"""
Skeletal system prototype class
"""

class SkeletalSystem():
    """
    Skeletal system manages bone density, and blood cell production
    """

    def __init__(self):
        self.bone_density = 8
        self.blood_cell_production_rate = 100

    def produce_blood_cells(self):
        """
        return some number, that represents a number of blood cells.
        """

        return 1000

    def increase_bone_density(self):
        """
        increase bone density
        """

        # Do not increase density above 10 [Does not go to Eleven]
        if self.bone_density < 10:
            self.bone_density += 1
            self.show_bone_density()
        else:
            print('Bones are as dense as possible')

    def decrease_bone_density(self):
        """
        decrease bone density
        """

        # Do not reduce bone density below 1
        if self.bone_density > 1:
            self.bone_density -= 1
            self.show_bone_density()
        else:
            print('Bones are as soft as possible')

    def show_bone_density(self):
        """
        print bone density to terminal
        """
        print('Bone Density: ' + str(self.bone_density))
