# test_json_structure.py
import json
import pytest
from pathlib import Path
from typing import Dict, Any


# Fixture to load JSON data
@pytest.fixture
def json_data(request) -> Dict[str, Any]:
    """Loads JSON data from path provided via command line"""
    json_path = request.config.getoption("--json-path")
    with open(json_path) as f:
        return json.load(f)


def test_required_fields(json_data):
    """Tests that all required fields are present"""
    required_fields = ["name", "age"]
    for field in required_fields:
        assert field in json_data, f"Missing required field: {field}"


def test_field_types(json_data):
    """Tests that fields have correct types"""
    assert isinstance(json_data["name"], str), "Name must be a string"
    assert isinstance(json_data["age"], (int, float)), "Age must be a number"


def test_field_constraints(json_data):
    """Tests that field values meet constraints"""
    assert len(json_data["name"]) > 0, "Name cannot be empty"
    assert json_data["age"] >= 0, "Age cannot be negative"
    assert json_data["age"] <= 150, "Age cannot be over 150"


def test_optional_fields(json_data):
    """Tests optional fields if present"""
    if "email" in json_data:
        assert "@" in json_data["email"], "Invalid email format"


def test_nested_structures(json_data):
    """Tests nested object structures if present"""
    if "address" in json_data:
        address = json_data["address"]
        assert isinstance(address, dict), "Address must be an object"
        assert "street" in address, "Address must have street"
        assert "city" in address, "Address must have city"


def test_array_fields(json_data):
    """Tests array fields if present"""
    if "phones" in json_data:
        phones = json_data["phones"]
        assert isinstance(phones, list), "Phones must be an array"
        for phone in phones:
            assert isinstance(phone, str), "Phone numbers must be strings"
            assert len(phone) >= 10, "Phone numbers must be at least 10 chars"
