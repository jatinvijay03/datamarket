"""Tests for helpers.py."""

import ckanext.datamarket.helpers as helpers


def test_datamarket_hello():
    assert helpers.datamarket_hello() == "Hello, datamarket!"
