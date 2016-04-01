print 'CSE 5243 Similarity Analysis by Kun Liu & Zhe Dong'

import load
(Data, Cnt, rdim, cdim) = load.load()

#convert data into 0/1
#for i in range(0, rdim):
#	for j in range(0, cdim):
#		if Data[i][j] != 0:
#			Data[i][j] = 1
#print "done1"

#compute true similarity
True_Sim = []
#import sklearn.metrics.pairwise
#Pair_Wise_Dist = sklearn.metrics.pairwise.pairwise_distances(Data,metric='jaccard')
#print "done2"

for i in range(0, rdim):
	print "document #"+str(i)
	row_sim = []
	for j in range(i+1, rdim):
		N = Data.getrow(i).dot(Data.getrow(j).transpose())
		U = Cnt[i]+Cnt[j]-N[0,0]
		sim = float(N[0,0])/float(U)
		row_sim.append(sim)
	True_Sim.append(row_sim)
print "done"

import minhash

M = minhash(cdim, 32)
