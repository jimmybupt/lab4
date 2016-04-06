from scipy.sparse import *

def load():
	vector_file = open('vector1.txt', 'r')

	import ast
	import sys
	info = open("info.txt",'r') #stores the number of vectors and length of vectors
	rdim = int(info.readline())
	cdim = int(info.readline())

	#M = lil_matrix((rdim, cdim))
	M = []
	C = []
	P = []

	print "Reading vectors... ",
	sys.stdout.flush()
	i = 0
	control = 0
	for line in vector_file:
		data = ast.literal_eval(line)
		cnt = 0
		V = [0] * cdim
		N = []
		for D in data:
			if float(D[1]) != 0.:
				V[int(D[0])] = 1
				N.append((int(D[0]),1))
				cnt += 1
		i=i+1
		if(cnt > 0 and control == 0):
			C.append(cnt)
			M.append(V)
			P.append(N)
		control = (control + 1) % 3
		if i==rdim:
			break

	#M = csr_matrix(M)
	print len(C)	
	print "done"
	return M, P, C, len(C), cdim
