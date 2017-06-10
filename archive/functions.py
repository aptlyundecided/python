# Practicing some functions.
"""Let's do some functions."""
#
# <<< Function Definitions >>>
#
# Add a new line
#
def newline():
    """Print a newline, for readabilities."""
    print("\n")
#
# Write a name.
#
def write_name(name):
    """First use of a parameter."""
    newline()
    print("My name is " + name)
#
#
#
def write_phrase(phrase):
    """Write an entire phrase."""
    newline()
    print(phrase)
#
# <<< Program Behavior >>>
#
write_name("Alex")
write_phrase("I think I'm going to enjoy using python to solve problems.")
write_phrase("I don't know if I'll use it without Django...")
write_phrase("But it's going to be useful in some way, I'm sure.")
newline()
