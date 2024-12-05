import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import add

def test_add():
    assert add(1,2) == 3
    assert add(1, "asdf") == "Invalid Input"

    # assert add(1,"abc") == "Invalid Input"