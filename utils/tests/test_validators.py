import pytest
from django.core.exceptions import ValidationError
from utils.validators import validate_positive_float, validate_is_date_before_today, validate_activity_level
from datetime import datetime, date, timedelta




##########################################################################TEST FOR VALIDATE_POSITIVE FLOAT##############################################################################################



@pytest.mark.parametrize("value, expected_exception", [
    (5.0, None),  # Positive float should pass without raising ValidationError
    (0, None),   # Zero is considered a positive float in this context
    (-0.1, ValidationError),  # Negative float should raise ValidationError
    ("string", ValidationError),  # Non-float value should raise ValidationError
    (-500.0, ValidationError),  # Another negative float should raise ValidationError
])
def test_validate_positive_float(value, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            validate_positive_float(value)
    else:
        # If expected_exception is None, the validation should pass without raising an exception
        validate_positive_float(value)

##############################################################################################################################################################################################    



#########################################################################TESTS FOR VALIDATE_IS_DATE_BEFORE_TODAY####################################################################3

#Various cases for validating
@pytest.mark.parametrize(
    "date_obj, expected_result",
    [
        # Valid cases for date objects
        (date.today() - timedelta(days=1), True),  # Date before today
        (date.today() - timedelta(days=365), True),  # Date before today
        (date.today(), False),  # Date same as today
        # Invalid cases for date objects
        (date.today() + timedelta(days=1), False),  # Date after today
        (date.today() + timedelta(days=365), False),  # Date after today
        
        # Valid cases for datetime objects
        (datetime.now() - timedelta(days=1), True),  # Date before today
        (datetime.now() - timedelta(days=365), True),  # Date before today
        (datetime.now(), False),  # Date same as today
        # Invalid cases for datetime objects
        (datetime.now() + timedelta(days=1), False),  # Date after today
        (datetime.now() + timedelta(days=365), False),  # Date after today
    ]
)
def test_is_date_before_today(date_obj, expected_result):
    assert validate_is_date_before_today(date_obj) == expected_result

    
##############################################################################################################################################################################################    



##############################################################################TESTS FOR VALIDATE_ACTIVITY_LEVEL################################################################################3
@pytest.mark.django_db
@pytest.mark.parametrize(
    "activity_level, is_valid",
    [
        (1, True),  # Valid activity level
        (2, True),  # Valid activity level
        (3, True),  # Valid activity level
        (4, True),  # Valid activity level
        (0, False),  # Invalid activity level
        (5, False),  # Invalid activity level
        (-3, False),  # Invalid activity level
    ]
)
def test_validate_activity_level(activity_level, is_valid):
    try:
        validate_activity_level(activity_level)
        assert is_valid, f"No ValidationError raised for activity level {activity_level}"
    except ValidationError:
        assert not is_valid, f"ValidationError raised for activity level {activity_level}"
        
        ##############################################################################################################################################################################################    
