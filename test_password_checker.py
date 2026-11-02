from password_checker import is_long_enough, is_strong


def test_strong_password():
    assert is_strong("Hello1234") is True


def test_too_short():
    assert is_strong("Ab1") is False


def test_no_digit():
    assert is_strong("HelloWorld") is False


def test_no_uppercase():
    assert is_strong("hello1234") is False


def test_length_boundary():
    assert is_long_enough("1234567") is False
    assert is_long_enough("12345678") is True
