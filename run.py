print 'CSE 5243 Similarity Analysis by Kun Liu & Zhe Dong'

import load
import minhash
import time

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


#compute hash similarity
start_time = time.time()
K=32 # number of hash functions
M = minhash.minhash(cdim, K)
Signatures = []
for D in Data:
	S = M.sig(Data[i])
	Signatures.append(S)
 
print "Creating signiture took  "+str(time.time() - start_time)+" seconds"

start_time = time.time()
Hash_Sim = []
for i in range(0, rdim):
	row_sim = []
	for j in range(i, rdim):
		N = 0
		for k in range(0, K):
			if(Signatures[i][k]==Signatures[j][k]):
				N += 1
		row_sim.append(N)
	Hash_Sim.append(row_sim)

print "Hash similarity calculation took  "+str(time.time() - start_time)+" seconds"

start_time=time.time()
print ""
print "MSE between the estimate and the true similarity is "+str(similarity_MSE(True_Sim,Hash_Sim))
print "Comparision took " +str(time.time() - start_time)+" seconds"
