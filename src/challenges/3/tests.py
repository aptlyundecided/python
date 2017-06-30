"""Unit tests with Python"""
import datetime

# Create your function that returns the day of the week as an integer
def what_day():
    """Return an integer, representing the day of the week"""

    # 0 - 6 [Mon - Sun]
    return datetime.datetime.today().weekday()

# Test to make sure it's friday (4 == Friday)
def test_answer():
    """unit test for what_day - expects 4"""
    assert what_day() == 4

"""
Printing results is un-needed!
Executing this code is different:
Instead of 'python yourfilename.py'
Use 'py.test yourfielname.py'
and you'll either see your file pass, or fail!
"""
