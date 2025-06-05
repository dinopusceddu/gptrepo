import pytest
from validator import validate_inputs, calculate, ValidationError

RULES = {
    "a": (0, 10),
    "b": (1, 5),
}

def test_validate_success():
    valid, errors = validate_inputs({"a": 5, "b": 2}, RULES)
    assert valid is True
    assert errors == {}

def test_validate_failure_out_of_range():
    valid, errors = validate_inputs({"a": 15, "b": 2}, RULES)
    assert not valid
    assert "a" in errors
    assert errors["a"] == "'a' deve essere compreso tra 0 e 10."

def test_calculate_blocks_on_invalid():
    with pytest.raises(ValidationError):
        calculate({"a": -1, "b": 3}, RULES)

