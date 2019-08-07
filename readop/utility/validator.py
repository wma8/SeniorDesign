"""
Contains functionality for validating data types.
"""


def validate_string(value: str) -> str:
    """
    Validates that the input value is a string.

    :param value: Value to check.
    :return: The input value if validation was successful.
    :raises TypeError: If the input value was not a str instance.
    """

    if not isinstance(value, str):
        raise TypeError('value must be instance of type str, received ' + str(type(value)))
    return value


def validate_string_not_empty(value: str) -> str:
    """
    Validates that the input value is a string and not empty.

    :param value: Value to check.
    :return: The input value if validation was successful.
    :raises ValueError: If the input value was empty.
    """

    validate_string(value)
    if not value:
        raise ValueError('value must not be empty')
    return value


def validate_int(value: int) -> int:
    """
    Validates that the input value is an integer.

    :param value: Value to check.
    :return: The input value if validation was successful.
    :raises TypeError: If the input value was not an int instance.
    """

    if not isinstance(value, int):
        raise TypeError('value must be instance of type int, received ' + str(type(value)))
    return value


def validate_int_geq_zero(value: int) -> int:
    """
    Validates that the input value is an integer and greater than or equal to zero.

    :param value: Value to check.
    :return: The input value if validation was successful.
    :raises ValueError: If the input value was less than zero.
    """

    validate_int(value)
    if not value >= 0:
        raise ValueError('value must be greater or equal to zero')
    return value


def validate_bool(value: bool) -> bool:
    """
    Validates that the input value is a boolean.

    :param value: Value to check.
    :return: The input value if validation was successful.
    :raises TypeError: If the input value was not a bool instance.
    """

    if not isinstance(value, bool):
        raise TypeError('value must be instance of type bool, received ' + str(type(value)))
    return value


def validate_credentials(value):
    """
    Validates that the input value is a valid set of credentials. This requires it to have
    username and password attributes. The username must be a non-empty string and the password
    must be a string (potentially empty).

    :param value: Value to check.
    :return: The input value if validation was successful.
    :raises AttributeError: If the input value does not have both a username and a password.
    """

    if not hasattr(value, 'username'):
        raise AttributeError('credentials must have username attribute')

    if not hasattr(value, 'password'):
        raise AttributeError('credentials must have password attribute')

    validate_string_not_empty(value.username)
    validate_string(value.password)

    return value
