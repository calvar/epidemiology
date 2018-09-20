##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Initially, there are N0 nodes connected randomly to one another (prob. p0).
## New nodes are added one by one. The prob of the new node to connect with an 
## existingnode i is pi=ki/sum_j kj. Where kj is the degree (No. of connections) 
## of node j. (Barabasi and Albert model)

from numpy import random
import math
import sys
from triangular import Triangular

# No. of nodes
N = 1024

# No. of  nodes in the initial network
N0 = 256

# No. of highly connected (HC) nodes in the initial network
Nhci = 10

# prob. of links between non HC nodes in the same initial cluster
pnhc = 0.37

# prob. of links between initial (HC) nodes
phc = 0.5

#Link counter
lnkcnt = [0 for i in range(N)]

###Link matrix
##links = Triangular(N)

#link list
llinks = []

#Generate initial network
clsize = N0 / Nhci
N0 = Nhci * clsize
nodes = [i for i in range(N0)]
clusters = [[] for i in range(Nhci)]
for n in range(Nhci):
    for j in range(clsize):
        rnd = random.randint(0,len(nodes))
        k = nodes[rnd]
        clusters[n].append(k)
        nodes.remove(k)
print(clusters)

for n in range(Nhci):
    #connect to HC node
    hcn = clusters[n][0]
    for a in range(1,clsize):
        i = clusters[n][a]
        lnkcnt[hcn] += 1
        lnkcnt[i] += 1 
        #	    print(str(i)+" "+str(j)+"\n")
        #	    links.set_element(i,j,1)
        pair = [min(i,j),max(i,j)]
        llinks.append(pair)
    #connect among other nodes
    for a in range(1,clsize-1):
        i = clusters[n][a]
        for b in range(a+1,clsize):
            j = clusters[n][b]
            rnd = random.random()
            if rnd < pnhc:
                lnkcnt[i] += 1
                lnkcnt[j] += 1 
                pair = [min(i,j),max(i,j)]
                llinks.append(pair)
for n in range(Nhci-1):
    #connect among HC nodes
    i = clusters[n][0]
    for m in range(n+1,Nhci):
        j = clusters[m][0]
        rnd = random.random()
        if rnd < phc:
            lnkcnt[i] += 1
            lnkcnt[j] += 1 
            pair = [min(i,j),max(i,j)]
            llinks.append(pair)
            
	    
#Add new nodes
for i in range(N0,N):
    #total number of links
    sum_l = sum(lnkcnt)
    for j in range(len(lnkcnt)-1):
        pair = [min(i,j),max(i,j)]
        prob = float(lnkcnt[j]) / sum_l
        if random.random() < prob:
            lnkcnt[i] += 1
            lnkcnt[j] += 1
            #	    print(str(i)+" "+str(j)+"\n")
            #	    links.set_element(i,j,1)
            llinks.append(pair)

print(lnkcnt)
print(float(sum(lnkcnt))/N)

ff = open('connlist.dat', 'w')
for i in xrange(len(llinks)):
    ff.write(str(llinks[i][0])+" "+str(llinks[i][1])+"\n")
ff.close()

#histogram
hist = [0 for i in xrange(N)]
for i in lnkcnt:
    hist[i] += 1
    
hf = open('deg_hist.dat', 'w')
for i in xrange(N):
    hf.write(str(i)+' '+str(hist[i])+'\n')
hf.close()
