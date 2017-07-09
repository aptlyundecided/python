"""Test the Greendale Human Being prototype"""

from characters.human_being import HumanBeing


def test_human_being():
    """Unit Tests for Human Being Prototype"""

    # Create human being class
    clark_smith = HumanBeing('Leonard', 'Rodriguez')

    # Assert that full name was assigned
    assert clark_smith.get_full_name() == 'Leonard Rodriguez'
