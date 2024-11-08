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
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "value"}
            goc = GithubOrgClient("org_name")
            self.assertEqual(goc._public_repos_url, "value")
