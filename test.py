"""
This module contains some test cases.
"""

from rbo import RankingSimilarity

if __name__ == '__main__':

	# test 1, this is from the fig.5 for the RBO paper
	print('Run test 1...')
	S = list('abcdefg')
	T = list('zcavwxy')

	RS = RankingSimilarity(S, T)
	print('The implemented answer is: {:6.3f}'.format(RS.rbo(p=1.0)))
	print('The correct answer is:      0.312')