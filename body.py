"""
Create the body class, using body system classes
"""
from digestive import DigestiveSystem
from skeletal import SkeletalSystem

class Body(SkeletalSystem, DigestiveSystem):
    """
    create a body, from various body systems.
    """

    def __init__(self):
        SkeletalSystem.__init__(self)
        DigestiveSystem.__init__(self)


# [!] Run Tests (pytest) [!]

def test_body():
    """
    tests for body class
    """
    new_body = Body()

    # Check initialized values
    assert new_body.blood_cell_production_rate == 100
    assert new_body.bone_density == 8
    assert new_body.hunger_level == 0

    # Check increase to bone density
    new_body.increase_bone_density()
    assert new_body.bone_density == 9

    # Check decrease to bone density
    new_body.decrease_bone_density()
    assert new_body.bone_density == 8

    # Check increase to hunger level
    new_body.increase_hunger_level()
    assert new_body.hunger_level == 1

    # Check decrease to hunger level
    new_body.eat_food()
    assert new_body.hunger_level == 0
