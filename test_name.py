# The simplest function to get the user email (copy to src/user_functions.py)
def get_name_from_input():
    """ not empty with no spaces"""
    return input("Write down your name: ")

# More elaborated version (copy to src/user_functions.py)
def get_name_from_input():
    """not empty with no spaces"""
    name = input("Write down your name: ")

    if (not name or " " in name):
        print('Name is not valid.')
    else:
        return name

# Tests (copy to tests/test_user_functions.py)
import pytest
import io
#from user_functions import *

def test_name_with_user_input_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(' '))
    assert get_name_from_input() is None

def test_name_with_user_input_with_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Mar ah'))
    assert get_name_from_input() is None

def test_name_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Marah'))
    assert get_name_from_input() == 'Marah'

# Do the same for the following functions
# Functions in src/user_functions.py and tests in tests/test_user_functions.py

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    return input("Create your user name: ")

def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    return input("Create your password: ")

