
from django.core.exceptions import ValidationError

def validate_positive_float(value):
    try:
        float_value = float(value)
    except (TypeError, ValueError):
        raise ValidationError(
            'Value must be a valid float or convertible to float',
            params={'value': value},
        )

    if float_value < 0:
        raise ValidationError(
            'Value must be a positive float',
            params={'value': value},
        )