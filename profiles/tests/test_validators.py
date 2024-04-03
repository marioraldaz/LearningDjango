import pytest
from django.core.exceptions import ValidationError
from ..utils.validators import validate_positive_float

@pytest.mark.parametrize("value, expected_exception", [
    (5.0, None),  # Positive float should pass without raising ValidationError
    (0, None),    # Zero is considered a positive float in this context
    (-0.1, ValidationError),  # Negative float should raise ValidationError
    ("string", ValidationError),  # Non-float value should raise ValidationError
    (-3.0, ValidationError),  # Another negative float should raise ValidationError
])
def test_validate_positive_float(value, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            validate_positive_float(value)
    else:
        # If expected_exception is None, the validation should pass without raising an exception
        validate_positive_float(value)
