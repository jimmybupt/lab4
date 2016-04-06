import numpy as np

class minhash:
	def __init__(self, size, k):
		self.size = size
		self.k = k
		self.perm = []
		for i in range(0,k):
			self.perm.append(np.random.permutation(size))
	
	def sig(self, vector):
		hash = []
		for i in range(0, self.k):
			for j in range(0, self.size):
				if vector[self.perm[i][j]] > 0:
					hash.append(j)
					break
		return hash
