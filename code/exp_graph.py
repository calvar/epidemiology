##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Create a random conectivity matrix in which each edge is included with
## exponential probability, assuming no correlations (Bernoulli graph).

import numpy as np
from numpy import random
import sys
from triangular import Triangular

# No. of nodes
N = 1024

#average
t = 5.4

#Link counter
lnkcnt = [0 for i in xrange(N)]

###Link matrix
##links = Triangular(N)

#link list
llinks = []

#list with number of connections
c = [int(np.floor(random.exponential(t))) for i in range(N)]
for i in range(N): 
    c[i] -= 1
    if c[i] < 0: c[i] = 0
#print(c)

#make the links
for i in xrange(N):
    lst = [k for k in range(N)]
    lst.remove(i)
    for k in range(c[i]-lnkcnt[i]):
        test = False
        cn = 0
        while not test:
            j = random.choice(lst)
            if lnkcnt[j] < c[j]: 
                pair = [min(i,j),max(i,j)]
                lst.remove(j)
                lnkcnt[i] += 1
                lnkcnt[j] += 1
                llinks.append(pair)
                test = True
            else:
                if cn > 10: test = True
            cn += 1

print(lnkcnt)
print(float(sum(lnkcnt))/N)

# dif = [c[i]-lnkcnt[i] for i in range(N)]
# print(dif)

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
