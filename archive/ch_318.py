# Challenge number 318
"""Challenge number 318 from r/daily_programmer"""
from itertools
#
# The first five items should have a way to use any mathematical operation
# on them, to equal the 6th number.
#
LIST1 = [25, 100, 9, 7, 3, 7, 881]
#
# BRUTE FORCE
#
TARGET = LIST1[6]
LIST1.remove(LIST1[6])
#
# Create a type list, meaning, the type of operator to be applied.
#
TYPE_LIST = ['A', 'A', 'A', 'A', 'A', 'A']
#
## Function Declarations ##
#
def add_two(num1, num2):
    """Add two numbers"""
    return num1 + num2

def subtract_two(num1, num2):
    """Subtract num1 from num2"""
    return num1 - num2

def multiply_two(num1, num2):
    """Multiply two numbers"""
    return num1 * num2

def divide_two(num1, num2):
    """divide num1 by num2"""
    return num1 / num2

def cycle_operator(index):
    """cycle operator to next available"""
    if TYPE_LIST[index] == 'A':
        TYPE_LIST[index] = 'S'
    elif TYPE_LIST[index] == 'S':
        TYPE_LIST[index] = 'M'
    elif TYPE_LIST[index] == 'M':
        TYPE_LIST[index] = 'D'
    elif TYPE_LIST[index] == 'D':
        print('End Cycle')
    else:
        print('Error @ cycle operator')
#
#
#
#### THEORY TEST
def run_numbers():
    """Tests"""
    pos1 = 0
    res = 0
    while pos1 < len(LIST1):
        if TYPE_LIST[pos1] == 'A':
            res = add_two(LIST1[pos1], res)
        elif TYPE_LIST[pos1] == 'S':
            res = subtract_two(res, LIST1[pos1])
        elif TYPE_LIST[pos1] == 'M':
            res = multiply_two(LIST1[pos1], res)
        elif TYPE_LIST[pos1] == 'D':
            res = divide_two(res, LIST1[pos1])
        pos1 += 1
    return res
#
#
#
print(run_numbers())
