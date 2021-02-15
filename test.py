"""
This module contains some test cases.
"""
import string

import numpy as np

from rbo import RankingSimilarity

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


def generate_tests():
    for S, T, expected in TESTS:
        yield list(S), list(T), expected


if __name__ == '__main__':
    p = 0.95
    for index, (S, T, expected) in enumerate(generate_tests()):
        print('\n===== Test {} ====='.format(index + 1))
        print('List 1 is: {}'.format(S))
        print('List 2 is: {}'.format(T))

        RS = RankingSimilarity(S, T, verbose=True)
        rbo = RS.rbo(p=1.0)
        print('The implemented Average Overlap is: {:6.3f}'.format(rbo))
        print('The correct answer is:              {:6.3f}'.format(expected))
        assert np.round(rbo, decimals=3) == expected

        print('The implemented rbo_ext 1 is: {:6.3f}'.format(
            RS.rbo(p=p, k=3, ext=True)))
        print('The implemented rbo_ext 2 is: {:6.3f}'.format(
            RS.rbo_ext(p=p)))
