"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.datamarket.logic import validators


def test_datamarket_reauired_with_valid_value():
    assert validators.datamarket_required("value") == "value"


def test_datamarket_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.datamarket_required(None)
