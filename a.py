"""a test"""

import human_being as human_being


def test_human_being():
    """Unit Tests for Human Being Prototype"""

    # Create human being class
    clark_smith = human_being.HumanBeing('Clark', 'Smith')

    # Assert that full name was assigned
    assert clark_smith.get_full_name() == 'Clark Smith'
