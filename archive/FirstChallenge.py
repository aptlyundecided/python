#
# First code challenge from reddit!
#
# Spoiler alert.  I looked at an answer in the comments, because I didn't
# understand the goal, and also I have no idea what I am doing in python yet.
"""Collatz Sequence?"""
#
# What is a collatz sequence.
#
def collatz_function(mahstring):
    """Do the damn thing."""
    #
    # This seems to be structured just like a Javascript object.
    # Success!  Concept understood.
    #
    pattern = {
        "a":"bc",
        "b": "a",
        "c": "aaa"
    }
    #
    # Loop-de-loop
    # NOTE there is a colon after the 1
    #
    while len(mahstring) > 1:
        #
        # NOTE there is a colon in the brackets, after the 2
        #
        #
        # TO DO
        # 01: why is there a colon after the first indirect reference.
        mahstring = mahstring[2:] + pattern[mahstring[0]]
        #
        # print the new string!
        #
        print(mahstring)
#
# Call zee function
#
collatz_function("aaa")
