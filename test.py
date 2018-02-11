"""
This module contains some test cases.
"""

from rbo import RankingSimilarity

if __name__ == '__main__':

	Ss = [
			list('abcdefghijklmnopqrstuvwxyz'),  # sanity check
			list('abcdefg'),	 # this is from the fig.5 for the RBO paper
			list('abcdefghijklmnopqrstuvwxyz'),
			list('abcde'),  # this is from  https://ragrawal.wordpress.com/2013/01/18/comparing-ranked-list/
			list('abcde'),  # this is from  https://ragrawal.wordpress.com/2013/01/18/comparing-ranked-list/
			]
	Ts = [
			list('abcdefghijklmnopqrstuvwxyz'),
			list('zcavwxy'),
			list('abcdefg'),
			list('bacde'),
			list('abced'),
			]
	As = [
			1.,
			0.312,
			1,
			0.8,
			0.95
	]

	p = 0.95

	for i in range(len(Ss)):
		print('\n===== Test {} ====='.format(i+1))
		print('List 1 is: {}'.format(Ss[i]))
		print('List 2 is: {}'.format(Ts[i]))

		RS = RankingSimilarity(Ss[i], Ts[i])
		print('The implemented Average Overlap is: {:6.3f}'.format(RS.rbo(p=1.0)))
		print('The correct answer is:              {:6.3f}'.format(As[i]))

		print('The implemented rbo_ext is: {:6.3f}'.format(RS.rbo_ext(p=p)))

