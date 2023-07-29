import pytest
from app.managers._endpoint_handler._util import (
    ensure_attributes_are_valid,
    ensure_string_is_valid_and_return_lower,
)

attrs_upper = {"One": ["String", 100], "Two": ["Integer"]}
attrs_lower = {"one": ["string", 100], "two": ["integer"]}
attrs_invalid = {"string": []}


def test_invalid_attributes_empty_list():
    with pytest.raises(AssertionError, match="Value cannot be an empty list"):
        ensure_attributes_are_valid({"one": []})


def test_invalid_attributes_not_a_list():
    with pytest.raises(AssertionError, match="Value needs to be a list"):
        ensure_attributes_are_valid({"one": "oo"})


def test_invalid_attributes_list_contains_more_than_two():
    with pytest.raises(AssertionError, match="Value cannot have more than 2 items"):
        ensure_attributes_are_valid({"one": ["ff", 12, 3, 4]})


def test_invalid_attributes_first_item_not_a_string():
    with pytest.raises(
        AssertionError, match="First item in passed value needs to be a string type"
    ):
        ensure_attributes_are_valid({"one": [22, 12]})
    with pytest.raises(
        AssertionError, match="First item in passed value needs to be a string type"
    ):
        ensure_attributes_are_valid({"one": [22, "oo"]})


def test_invalid_attributes_second_item_not_int():
    with pytest.raises(
        AssertionError, match="Second item in passed value needs to be a integer type"
    ):
        ensure_attributes_are_valid({"one": ["dd", "ww"]})


def test_ensure_attributes_are_valid():
    assert attrs_lower == ensure_attributes_are_valid(attrs_upper)


def test_ensure_attrs_are_valid_invalid_keys():
    with pytest.raises(ValueError, match=f"Value string is forbiden"):
        ensure_attributes_are_valid(attrs_invalid)


def test_raises_value_error_if_item_found_in_foribden_names():
    with pytest.raises(ValueError, match=f"Value string is forbiden"):
        ensure_string_is_valid_and_return_lower("string")


def test_return_lower_after_validation():
    item1 = "KDJDKDK"
    item2 = "kdMDndJD"
    item3 = "sdfsdfdsf"

    item1_test = ensure_string_is_valid_and_return_lower(item1)
    item2_test = ensure_string_is_valid_and_return_lower(item2)
    item3_test = ensure_string_is_valid_and_return_lower(item3)

    assert item1_test == item1.lower()
    assert item2_test == item2.lower()
    assert item3_test == item3.lower()


def test_ensure_passed_string_contains_letters_only():
    item1 = "SKnd112"
    item2 = "123KSN34"
    item3 = "kd$ms@_1"

    with pytest.raises(ValueError, match="Must contain only letters"):
        ensure_string_is_valid_and_return_lower(item1)
    with pytest.raises(ValueError, match="Must contain only letters"):
        ensure_string_is_valid_and_return_lower(item2)
    with pytest.raises(ValueError, match="Must contain only letters"):
        ensure_string_is_valid_and_return_lower(item3)
