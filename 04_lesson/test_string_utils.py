import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("saint-Petersburg", "Saint-Petersburg"),
    ("   ", "   "),
    ("", ""),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
    
    
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("   hello world", "hello world"),
    ("   ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   sky pro", "sky pro"),
    ("skypro   ", "skypro   "),
    ("\nskypro", "\nskypro"),
    (" \t \n skypro", "\t \n skypro"),
     ("@#$%", "@#$%"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected
    
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "S"),
    ("abbaa", "a"),
    ("Hello World", " "),
    ("123abc", "2"),
    ("test@test.com", "@"),
])
def test_contains_positive(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is True
    
    
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "U"),
    ("SkyPro", "Y"),
    ("SkyPro", "sky"),
    ("", "a"),
    ("aa", "aaa"),
])
def test_contains_negative(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is False
    
    
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
     ("SkyPro", "k", "SyPro"),
     ("SkyPro", "ky", "SPro"),
     ("banana", "a", "bnn"),
     ("Hello World", " ", "HelloWorld"),
     ("abc123", "1", "abc23"),
     ("test@email.com", "@", "testemail.com"),
     ("test", "test", ""),
      ("aa", "a", ""),
      ])
def test_delete_symbol_positive(input_str, symbol, expected):
    actual_result = string_utils.delete_symbol(input_str, symbol)
    assert actual_result == expected
    
    
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
     ("SkyPro", "z", "SkyPro"),
      ("SkyPro", "sky", "SkyPro"),
      ("SkyPro", "SkyProg", "SkyPro"),
      ("", "a", ""),
      ])
def test_delete_symbol_negative(input_str, symbol, expected):
    actual_result = string_utils.delete_symbol(input_str, symbol)
    assert actual_result == expected