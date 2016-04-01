print 'CSE 5243 Similarity Analysis by Kun Liu & Zhe Dong'

import load
(Data, rdim, cdim) = load.load()

#convert data into 0/1
for i in range(0, rdim):
	for j in range(0, cdim):
		if Data[i][j] != 0:
			Data[i][j] = 1

#compute true similarity
True_Sim = []
for i in range(0, rdim):
	row_sim = []
	for j in range(i+1, rdim):
		U = 0
		N = 0
		for k in range(0, cdim):
			l = Data[i][k]
			r = Data[j][k]
			if l>0 or r>0:
				U += 1
				if l==r:
					N += 1
		sim = float(N)/float(U)
		row_sim.append(sim)
	True_Sim.append(row_sim)

import minhash

