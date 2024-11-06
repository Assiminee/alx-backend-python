#!/usr/bin/env python3
"""
Module defining tests for
"""
import unittest
from typing import Tuple, Dict, Union
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()