"""A tiny password strength checker used for the CI/CD demo."""


def is_long_enough(password):
    """Password must have at least 8 characters."""
    return len(password) >= 8


def has_digit(password):
    """Password must contain at least one digit."""
    return any(ch.isdigit() for ch in password)


def has_uppercase(password):
    """Password must contain at least one uppercase letter."""
    return any(ch.isupper() for ch in password)


def is_strong(password):
    """A strong password is long enough AND has a digit AND has an uppercase letter."""
    return is_long_enough(password) and has_digit(password) and has_uppercase(password)
