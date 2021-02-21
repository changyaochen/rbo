"""
This module contains some test cases.
"""
import string

import numpy as np
import pytest
from rbo.rbo import RankingSimilarity

TESTS = [
    # Sanity checks
    (string.ascii_lowercase, string.ascii_lowercase, 1.0),
    (string.ascii_lowercase, string.ascii_lowercase[:7], 1.0),
    ('abcde', 'fghij', 0.0),

    # RBO Paper Figure 5
    ('abcdefg', 'zcavwxy', 0.312),

    # Source:  https://ragrawal.wordpress.com/2013/01/18/comparing-ranked-list/
    ('abcde', 'bacde', 0.8),
    ('abcde', 'abced', 0.95),

    # One-Element lists
    ('a', 'a', 1.0),
    ('a', 'b', 0),

    # Empty lists
    ('', '', 1),
    ('a', '', 0),
    ('', 'a', 0),
]


@pytest.mark.parametrize('list_1, list_2, expected', TESTS)
def test_rbo(list_1: list, list_2: list, expected: float):
    """
    Args:
        list_1: List 1.
        list_2: List 2.
        expected: Expected RBO.

    Returns:
        None
    """
    p = 0.95  # pylint: disable=invalid-name
    list_1, list_2 = list(list_1), list(list_2)
    print('List 1 is: {}'.format(list_1))
    print('List 2 is: {}'.format(list_2))

    rs_object = RankingSimilarity(list_1, list_2, verbose=True)
    rbo = rs_object.rbo(p=1.0)
    print('The implemented Average Overlap is: {:6.3f}'.format(rbo))
    print('The correct answer is:              {:6.3f}'.format(expected))
    assert np.round(rbo, decimals=3) == expected

    print('The implemented rbo_ext 1 is: {:6.3f}'.format(
        rs_object.rbo(p=p, k=3, ext=True)))
    print('The implemented rbo_ext 2 is: {:6.3f}'.format(
        rs_object.rbo_ext(p=p)))
