"""
The Human Being prototype represents characteristics that any person attending Greendale would have.
"""

class HumanBeing():
    """
    A Greendale Human Being.
    """

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.major = ''
        self.years_at_greendale = 0
        self.location = ''

    def get_full_name(self):
        """
        return f_name and l_name of human being instance, with a space between.
        """
        return self.f_name + ' ' + self.l_name
