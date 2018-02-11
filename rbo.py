"""
This module is to calculate various measures between 2 ranked lists

Changyao Chen
Feb. 2018
"""

from scipy.stats import kendalltau
import numpy as np

class ProgressPrintOut(object):

	def __init__(self, N):
		self.N = N

	def printout(self, i):
		print('\r', int(100.0*i / self.N), '%', end='')
		if i == self.N - 1:
			print('\nfinished!')



class RankingSimilarity(object):
	"""
	This class will include some similarity measures between two different ranked lists
	"""
	def __init__(self, S, T):
		"""
		Input
		=============
		S, T: <list>
			lists with alphanumeric elements. They could be of different lengths. 
			Both of the them should be ranked, i.e., each element's position reflects 
			its respective ranking in the list.

			Also we will require that there is no duplicate element in each list
		"""
		assert(type(S) in [list, np.ndarray])
		assert(type(T) in [list, np.ndarray])

		assert(len(S) == len(set(S)))
		assert(len(T) == len(set(T)))
		
		self.S, self.T = S, T
		self.N_S, self.N_T = len(S), len(T)


	def kendall(self):
		"""
		This is the scipy version of Kendall tau.
		https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.kendalltau.html
		Per the doc: 'This is the tau-b version of Kendall’s tau which accounts for ties'

		The Kendall tau can only handle conjoint cases, i.e. the elements in both lists
		should be the same. 
		"""
		
		common_elements = set(self.S) & set(self.T)
		N_c = len(common_elements)
		print('The number of common elements is {}'.format(N_c))
		print('The proportion used in list S is {:6.3f}%.'.format(100.0*N_c / self.N_S))
		print('The proportion used in list T is {:6.3f}%.'.format(100.0*N_c / self.N_T))
		
		def common_ranking(L, common_set):
			# need to build the ranking for the common section
			# the time complexity should be loglinear, due to the sorting
			# TODO: can it be faster?
			
			tmp_dict = {}
			for i, x in enumerate(L):
				if x in common_set:
					tmp_dict[x] = i

			# the item in the ranking is sorted, to be consistent
			L_rank = list(map(tmp_dict.get, sorted(tmp_dict.keys())))

			return L_rank

		S_rank = common_ranking(S, common_elements)
		T_rank = common_ranking(T, common_elements)					

		# print(S_rank)
		# print(T_rank)
		cor, pval = kendalltau(S_rank, T_rank)

		return cor

	def rbo(self, k=None, p=1.0):
		"""
		This the weighted non-conjoint measures, namely, rank-biased overlap.

		Unlike Kendall tau which is correlation based, this is intersection based.
		The implementation if from Eq. (4) or Eq. (7) (for p != 1) from the RBO paper
		http://www.williamwebber.com/research/papers/wmz10_tois.pdf

		If p=1, it returns to the un-bounded set-intersection overlap,
		according to Fagin et al.
		https://researcher.watson.ibm.com/researcher/files/us-fagin/topk.pdf

		The fig. 5 in that RBO paper can be used as test case.

		Note there the choice of p is of great importance, since it essentically
		control the 'top-weightness'. Simply put, to an extreme, a small p value will
		only consider first few items, whereas a larger p value will consider 
		more itmes. See Eq. (21) for quantitative measure.

		Input
		=============
		k: <int>, default None
			The depth of evaluation
		p: <float>, default 1.0
			weight of each agreement at depth d: p**(d-1)
			when set to 1.0, there is no weight, the rbo returns to average overlap

		Return
		============
		The rbo at depth k
		"""

		if k is None:
			k = float('inf')
		k = min(self.N_S, self.N_T, k)
		
		# initilize the agreement and average overlap arrays
		A, AO = [0 for _ in range(k)], [0 for _ in range(k)]
		if p == 1.0:
			weights = [1.0 for _ in range(k)]
		else:
			assert(0.0 < p < 1.0)
			weights = [1.0*(1-p)*p**d for d in range(k)]
		
		S_running, T_running = {self.S[0]: True}, {self.T[0]: True}  # using dict for O(1) look up
		A[0] = 1 if self.S[0] == self.T[0] else 0
		AO[0] = weights[0] if self.S[0] == self.T[0] else 0

		PP = ProgressPrintOut(k)
		for d in range(1, k):
			
			PP.printout(d)			
			tmp = 0
			# if the new item from S is in T already
			if self.S[d] in T_running:
				tmp += 1
			# if the new item from T is in S already
			if self.T[d] in S_running:
				tmp += 1
			# if the new itmes are the same, which also means the previous two cases didn't happen
			if self.S[d] == self.T[d]:
				tmp += 1

			# update the agreement array
			A[d] = 1.0*((A[d-1] * d) + tmp) / (d+1) 
			
			# update the average overlap array
			if p == 1.0:
				AO[d] = ((AO[d-1] * d) + A[d]) / (d+1)
			else: # weighted average
				AO[d] = AO[d-1] + weights[d] * A[d]

			# add the new item to the running set (dict)
			S_running[self.S[d]] = True 
			T_running[self.T[d]] = True

		return AO[-1]

if __name__ == '__main__':
	S = list('abcde')
	T = S[::-1][:3]
	
	RS = RankingSimilarity(S, T)
	print(RS.kendall())


