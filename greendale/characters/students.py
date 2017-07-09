"""Student prototype"""

from characters.human_being import HumanBeing

class Student(HumanBeing):
    """
    Student
    """

    def __init__(self, f_name, l_name):
        # For the extension to work properly, the init for human being must also be executed.
        HumanBeing.__init__(self, f_name, l_name)

        # Has this student already graduated?
        self.is_graduated = False
