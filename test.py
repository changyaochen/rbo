"""
This module contains some test cases.
"""

from rbo import RankingSimilarity

if __name__ == '__main__':

	Ss = [
			list('abcdefghijklmnopqrstuvwxyz'),  # sanity check
			list('abcdefghijklmnopqrstuvwxyz'),
			list('abcde'),
			list('abcdefg'),	 # this is from the fig.5 for the RBO paper
			list('abcde'),  # this is from  https://ragrawal.wordpress.com/2013/01/18/comparing-ranked-list/
			list('abcde'),  # this is from  https://ragrawal.wordpress.com/2013/01/18/comparing-ranked-list/
			list('a'),
			list('a')
			]
	Ts = [
			list('abcdefghijklmnopqrstuvwxyz'),
			list('abcdefg'),
			list('fghij'),
			list('zcavwxy'),
			list('bacde'),
			list('abced'),
			list('a'),
			list('b'),
			]
	As = [
			1.,
			1.,
			0.,
			0.312,
			0.8,
			0.95,
			1.,
			0,
	]

	p = 0.95

	for i in range(len(Ss)):
		print('\n===== Test {} ====='.format(i+1))
		print('List 1 is: {}'.format(Ss[i]))
		print('List 2 is: {}'.format(Ts[i]))

		RS = RankingSimilarity(Ss[i], Ts[i], verbose=True)
		print('The implemented Average Overlap is: {:6.3f}'.format(RS.rbo(p=1.0)))
		print('The correct answer is:              {:6.3f}'.format(As[i]))
		print('The implemented rbo_ext 1 is: {:6.3f}'.format(RS.rbo(p=p, k=3, ext=True)))
		print('The implemented rbo_ext 2 is: {:6.3f}'.format(RS.rbo_ext(p=p)))

