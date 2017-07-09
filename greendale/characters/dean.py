"""
The Dean, Craig Pelton singleton || should be an extension of the HumanBeing prototype.
"""

from characters.human_being import HumanBeing

# think of an item, of which there is ever only one at a time.
class Dean(HumanBeing):
    """
    A college has one Dean
    """

    def __init__(self, f_name, l_name):
        # For the extension to work properly, the init for human being must also be executed.
        HumanBeing.__init__(self, f_name, l_name)

        self.nickname = 'Dean'
        self.title = 'Dean'

        # the Dean must have office hours
        self.study_group_office_hours = ['00:00', '23:59']
        self.office_hours = [['08:00', '12:00'], ['14:00', '16:00']]

        # What costume is the Dean currently wearing?
        self.current_costume = 'Dean Outfit'

    # Deans must administrate, that's probably their most prominent role.
    def study_group_announcement(self):
        """Print a phrase from deans room_intro_announcements"""
        print('Ah! The duali-DEAN of man!')
