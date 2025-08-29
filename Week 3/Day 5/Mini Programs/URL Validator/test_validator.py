# test_validator.py
from validator import URLValidator

def test_valid_url():
    v = URLValidator()
    assert v.is_valid("https://example.com")

def test_invalid_url():
    v = URLValidator()
    assert not v.is_valid("ftp://wrong.com")
