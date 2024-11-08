#!/usr/bin/env python3
"""
Test module for client.py module
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test class for GithubOrgClient class """
    @parameterized.expand([
        ("google", ),
        ("abc", ),
    ])
    @patch('requests.get')
    def test_org(self, org, request_get_mock):
        """ Test method for org method """
        url = "https://api.github.com/orgs/{org}"
        mock_response = Mock()
        mock_response.org = org
        request_get_mock.return_value = mock_response

        get_json(url.format(org=org))
        request_get_mock.assert_called_once_with(url.format(org=org))

    def test_public_repos_url(self):
        """ method to unit-test GithubOrgClient._public_repos_url """
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": "value"}
            goc = GithubOrgClient("org_name")
            self.assertEqual(goc._public_repos_url, "value")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ method to unit-test GithubOrgClient.public_repos """
        test_payload = {
            'repos_url': "https://api.github.com/users/assimine/repos",
            'repos': [
                {
                    "id": 1918182,
                    "name": "rep.1",
                    "private": True,
                    "owner": {
                        "login": "assimine",
                        "id": 92039,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/assimine/rep.1",
                    "created_at": "2022-11-01T00:31:37Z",
                    "updated_at": "2023-09-23T11:53:58Z",
                    "has_issues": False,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 111111,
                    "name": "rep.2",
                    "private": False,
                    "owner": {
                        "login": "assimine",
                        "id": 92039,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/assimine/rep.2",
                    "created_at": "2020-03-04T22:52:33Z",
                    "updated_at": "2024-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 101,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch.object(
                GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_pub:
            mock_pub.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("assimine").public_repos(),
                [
                    "rep.1",
                    "rep.2"
                ],
            )
            mock_pub.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "ln-5-13"}}, "ln-5-13", True),
        ({'license': {'key': "some-licence"}}, "not-the-same-licence", False),
    ])
    def test_has_license(self, repo, key, expected):
        """Tests the has_license method."""
        gh_org_client = GithubOrgClient("assimine")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)
