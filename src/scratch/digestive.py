"""
Digestive system prototype class
"""

class DigestiveSystem():
    """
    Digestive takes food and turns it into energy.
    """

    def __init__(self):
        self.hunger_level = 0



    def eat_food(self):
        """
        when food is eaten, hunger level reduces
        """

        if self.hunger_level > 0:
            self.hunger_level -= 1
            self.show_hunger_level()
        else:
            print('Too full to eat anymore.')



    def show_hunger_level(self):
        """
        display hunger level to console
        """
        print(self.hunger_level)



    def increase_hunger_level(self):
        """
        increase hunger level
        """

        if self.hunger_level < 10:
            self.hunger_level += 1
            self.show_hunger_level()
        else:
            print('Cannot become hungrier without starvation')
