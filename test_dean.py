"""
Test the Dean singleton.
Should extend the class human being
"""

import dean as dean


def test_dean():
    """
    test for dean-ness
    """
    craig_pelton = dean.Dean('Craig', 'Pelton')

    assert craig_pelton.get_full_name() == 'Craig Pelton'
    assert craig_pelton.nickname == 'Dean'
    assert craig_pelton.title == 'Dean'
