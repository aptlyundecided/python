"""Unit tests with Python"""
import datetime

def what_day():
    """Return an integer, representing the day of the week"""

    # 0 - 6 [Mon - Sun]
    return datetime.datetime.today().weekday()


def test_answer():
    """unit test for what_day - expects 4"""
    assert what_day() == 4

print(test_answer())
