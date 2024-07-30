import pytest
from datetime import datetime

def add(a, y):
    return a + y

def test_add():
    print("teste_add", datetime.now())
    assert add(1,1) == 2

def test_fail_add():
    print("test_fail_add", datetime.now())
    assert add(1,2) != 2
