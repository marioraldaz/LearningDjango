from django.core.exceptions import ValidationError
from datetime import datetime, date


def validate_positive_float(value):
    if isinstance(value, (float, int)):
        float_value = float(value)  # Convert to float if it's an integer
    elif isinstance(value, str) and value.replace('.', '', 1).isdigit():
        float_value = float(value)
    else:
        raise ValidationError(
            'Value must be a valid float or convertible to float',
            params={'value': value},
        )

    print(value)
    if float_value < 0:
        raise ValidationError(
            'Value must be a positive float or integer',
            params={'value': value},
        )
def validate_is_date_before_today(date_obj):
    """
    Check if the given date is before today.

    Args:
    - date_obj: A datetime.date or datetime.datetime object representing the date.

    Returns:
    - True if the date is before today, False otherwise.
    """
    if isinstance(date_obj, (date, datetime)):
        try:
            current_date = date.today()
            if isinstance(date_obj, datetime):
                date_obj = date_obj.date()  # Extract date part from datetime object
            return date_obj < current_date
        except ValueError:
            return False
    else:
        return False
    
def validate_activity_level(value):
    """
    Validator function to ensure that the given value is an integer between 1 and 4.
    """
    if value < 1 or value > 4:
        raise ValidationError(('Activity level must be an integer between 1 and 4.'), code='invalid')
    