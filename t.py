"""
The Dean singleton || should be based on 'human being' singleton
"""

# think of an item, of which there is ever only one at a time.
class Dean():
    """
    A college has one Dean
    """

    def __init__(self, name):
        self.name = name | ''
        self.title = 'Dean'
        self.location = ''
        self.office_hours = []

    # Deans must administrate, that's probably their most prominent role.
    def administrate(self):
        """Print a phrase to terminal."""
        print('I\'m Administrating!')
        