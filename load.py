from scipy.sparse import *

def load():
	vector_file = open('vector1.txt', 'r')

	import ast
	import sys
	info = open("info.txt",'r') #stores the number of vectors and length of vectors
	rdim = int(info.readline())
	cdim = int(info.readline())

	M = lil_matrix((rdim, cdim))
	C = []

	print "Reading vectors... ",
	sys.stdout.flush()
	i = 0
	for line in vector_file:
		data = ast.literal_eval(line)
		cnt = 0
		for D in data:
			if float(D[1]) != 0.:
				M[i, int(D[0])] = 1
				cnt += 1
		i=i+1
		C.append(cnt)
		if i==rdim:
			break

	M = M.tocsr()	
	print "done"
	return M, C, rdim, cdim
