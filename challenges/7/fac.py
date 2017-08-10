"""Abstract Ant Factory"""

# [!] Declare ant properties [!]

# Base ant proerties
class BaseAnt():
    """This is a class that all ants will have."""
    def __init__(self):
        self.species = 'Ant'
        self.taxonomic_class = 'Insect'
        self.role = 'not assigned'
        self.hp = 150

    def show_role(self):
        """Print role to screen."""
        print('My role is to be a ' + self.role)

# Queen ant properties
class Queen(BaseAnt):
    """The queen of the ant colony."""
    def __init__(self):
        # Execute base class 'prototype'
        BaseAnt.__init__(self)

        # Assign role 'title'
        self.role = 'Queen'

        #
        self.hp += 1400

# Worker ant properties
class Worker(BaseAnt):
    """A worker in the ant colony."""
    def __init__(self):
        # Instantiate base class
        BaseAnt.__init__(self)

        # assign role
        self.role = 'Worker'

# Soldier ant properties
class Soldier(BaseAnt):
    """A Soldier of the ant colony."""
    def __init__(self):
        # Instantiate base class
        BaseAnt.__init__(self)

        # assign role
        self.role = 'Soldier'

        # modify hp
        self.hp += 400

# Drone ant properties
class Drone(BaseAnt):
    """A Drone of the ant colony."""
    def __init__(self):
        BaseAnt.__init__(self)
        self.role = 'Drone'
        self.hp -= 50

# 'Alate' ant properties
class Alate(BaseAnt):
    """An Alate from a colony. [DEFAULT FEMALE]"""
    def __init__(self, sex):
        BaseAnt.__init__(self)
        self.role = 'Alate'
        self.sex = sex
        self.hp += 50

    def is_male(self):
        """Make the Alate be a male."""
        self.sex = 'Male'

# Create the ant factory
class AntFactory(object):
    """The Ant Factory"""

    @staticmethod
    def new_ant(ant_type):
        """Create a new ant."""
        if ant_type == 'Queen':
            return Queen()
        elif ant_type == 'Worker':
            return Worker()
        elif ant_type == 'Soldier':
            return Soldier()
        elif ant_type == 'Drone':
            return Drone()
        elif ant_type == 'Alate':
            return Alate('Female')
        else:
            print('Ant type does not exist.')


# Create a list of ant types
ANT_TYPES = ['Queen', 'Worker', 'Soldier', 'Drone', 'Alate']

# Create an empty list
ANT_OBJECTS = []

# cycle through the types of ants, and create the correct ant object using the ant factory
for ant in ANT_TYPES:
    ANT_OBJECTS.append(AntFactory().new_ant(ant))

# Loop through
for i in range(len(ANT_TYPES)):
    ANT_OBJECTS[i].show_role()


# [!] END [!]
