import pytest
from datetime import datetime

def sub(x, y):
    return x - y

def test_sub():
    print("test_sub", datetime.now())
    assert sub(1,1) == 0

def test_fail_sub():
    print("test_fail_sub begin", datetime.now())
    import time; time.sleep(10)
    print("test_fail_sub final", datetime.now())
    assert sub(1,2) != 0
