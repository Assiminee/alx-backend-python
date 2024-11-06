#!/usr/bin/env python3
"""
Module defining tests for
"""
import unittest
from typing import Tuple, Dict, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for the method utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Dict,
            path: Tuple[str],
            expected_value: Union[int, Dict]
    ) -> None:
        """
        Test method for access_nested_map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_value)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str], exception: Exception) -> None:
        """
        Tests that a KeyError is raised for
        the inputs passed
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)



class TestGetJson(unittest.TestCase):
    """
    Test class for the method get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Tests method get_json using parameters
        passed using parameterized.expand
        """
        mock_response = Mock()

        mock_response.url = test_url
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)

        self.assertEqual(test_payload, result)
