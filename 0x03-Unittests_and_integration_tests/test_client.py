#!/usr/bin/env python3
"""
Test module for client.py module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


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
