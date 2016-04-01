def load():
	vector_file = open('vector1.txt', 'r')

	import ast
	import sys
	from scipy.sparse import *
	info = open("info.txt",'r') #stores the number of vectors and length of vectors
	rdim = int(info.readline())
	cdim = int(info.readline())

	M = lil_matrix((rdim, cdim))

	print "Reading vectors... ",
	sys.stdout.flush()
	i = 0
	for line in vector_file:
		data = ast.literal_eval(line)
		for D in data:
			M[offset, int(D[0])] = float(D[1])
		i=i+1
		if i==rdim:
			break

	M = M.toarray()	
	print "done"
	return M, rdim, cdim
