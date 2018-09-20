##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Create a regular conectivity matrix in which each edge is connected only
## with its nearest neighbors (lattice), using PBC. Then, reconnect each link 
## with probability p to a random node. (Watts and Strogatz model) 

from numpy import random
import math
import sys
#from triangular import Triangular

# No. of nodes
N = 1024

#link reconnection probability
p = 0.9

#Link counter
lnkcnt = [0 for i in xrange(N)]

###Link matrix
##links = Triangular(N)

#link list
llinks = []

#Square lattice
sq = math.sqrt(N)
sqint = int(sq)
if sq == sqint:
    for i in xrange(N):
	row = int(math.floor(float(i)/sqint))
	col = int(i - row * sqint)
      
	j = i + 1
	if random.random() >= p:
	    if col == sqint-1:  #PBC
		j -= sqint
	else: #reconnection
	    rnd = i
	    while rnd == i: 
		rnd = random.randint(N)
	    j = rnd
	
	k = i + sqint
	if random.random() >= p:
	    if row == sqint-1:  #PBC
		k -= sqint * sqint
	else: #reconnection
	    rnd = i
	    while rnd == i: 
		rnd = random.randint(N)
	    k = rnd
	
#	print(str(i)+" "+str(j)+" "+str(k)+"\n")
#	links.set_element(i,j,1)

	pair1 = [i,j]
	llinks.append(pair1)
	pair2 = [i,k]
	llinks.append(pair2)
	lnkcnt[i] += 2
	lnkcnt[j] += 1
	lnkcnt[k] += 1
else:
    print("Cannot form a square lattice!")

print(lnkcnt)

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

#f = open('connectivity.dat', 'w')
#for i in xrange(N):
#    for j in range(i+1,N):
#	f.write(str(links(i,j))+" ")
#    f.write("\n")
#f.close()
