"""Does single quote work?"""
#
#
class Letters:
    """Mah letters!"""
    list = ['A', 'A', 'B']

    def get_length(self):
        """Get length of list."""
        return len(self.list)

    def get_letters(self):
        """Get the list."""
        return self.list

    def add_letter(self, new_letter):
        """Add a letter to the list."""
        if isinstance(new_letter, (str)) == "string":
            print("string")
        else:
            # print(isinstance(new_letter))
            print('Fart')
#
LETTER_LIST = Letters()

print(LETTER_LIST.get_letters())
print(LETTER_LIST.add_letter('G'))
