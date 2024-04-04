from django.core.exceptions import ValidationError

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