# Let's learn about lists.
"""Let's learn a bit about lists"""
#
# Define the list
#
LIST1 = [1, 2, 3, 4, 5]
#
# APPEND
#
LIST1.append(6)
LIST1.append(7)
#
# Ah crap I added 7 instead of 6. This is ok.  Let's insert.
#
# At index 5, insert int 6
#
LIST1.insert(5, 6)
#
# I love this method.  It removes the first element that it matches.
#
LIST1.remove(6)
#
# I also love this method. get the index of an item by it's value
#
INDEX_OF_3 = LIST1.index(3)
print(INDEX_OF_3)
print(LIST1)
# END
