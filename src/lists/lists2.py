# Let's learn about lists.
"""Let's learn a bit about lists"""
#
# Define the list
#
LIST = [1, 2, 3, 4, 5]
LISTCOPY = LIST
#
# Print same if they are the same (should this be a function????!!!)
#
if LIST[2] == LISTCOPY[2]:
    print('same')
#
# Change the third index
#
LIST[2] = 345
#
# Show that the index is actually changed.
#
print(LIST[2])
#
# Print 'same' if they are the same.
#
if LIST[2] == LISTCOPY[2]:
    print('same')
