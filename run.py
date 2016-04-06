print 'CSE 5243 Similarity Analysis by Kun Liu & Zhe Dong'

import load
import minhash
import time
import numpy as np

(Data, SparseData, Cnt, rdim, cdim) = load.load()

#convert data into 0/1
#for i in range(0, rdim):
#	for j in range(0, cdim):
#		if Data[i][j] != 0:
#			Data[i][j] = 1
#print "done1"

#import sklearn.metrics.pairwise
#Pair_Wise_Dist = sklearn.metrics.pairwise.pairwise_distances(Data,metric='jaccard')
#print "done2"

#Mean Squared Error
def similarity_MSE(true_sim, hash_sim):
    mse = 0
    for i in range(0,len(true_sim)):
        for j in range(0, len(true_sim[i]) ):
            mse += pow(true_sim[i][j] - hash_sim[i][j],2)
    
    return mse / len(true_sim)
    
    
#compute true similarity
start_time = time.time()
print "Calculate true similarities"
True_Sim = []
for i in range(0, rdim):
	print "document #"+str(i)
	row_sim = []
	for j in range(i+1, rdim):
		#N = Data.getrow(i).dot(Data.getrow(j).transpose())
		N = 0
		for (a,b) in SparseData[j]:
			if Data[i][a] == 1:
				N += 1
		#N = np.inner(Data.getrow(i), Data.getrow(j))
		U = Cnt[i]+Cnt[j]-N
		sim = float(N)/float(U)
		row_sim.append(sim)
	True_Sim.append(row_sim)
print ""
print "True similarity calculation took  "+str(time.time() - start_time)+" seconds"

M = minhash.minhash(cdim, 32)
Signatures = []
for D in Data:
	S = M.sig(Data[i])
	Signatures.append(S)

Hash_Sim = []
for i in range(0, rdim):
	row_sim = []
	for j in range(i, rdim):
		N = 0
		for k in range(0, 32):
			if(Signatures[i][k]==Signatures[j][k]):
				N += 1
		row_sim.append(N)
	Hash_Sim.append(row_sim)
