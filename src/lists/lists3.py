# Let's learn about lists.
"""Let's learn a bit about lists"""
#
# Define the list
#
def list_maker():
    """list maker creates a list, then returns it"""
    new_list = [1, 2, 3, 4, 5]
    return new_list
#
# Assign the list to two variables.
#
LIST1 = list_maker()
LIST2 = list_maker()
#
# modify an item within the list.
#
LIST2[2] = 343
if LIST1[2] == LIST2[2]:
    print('same')
else:
    print('not same')
    print(LIST1)
    print(LIST2)
# END
