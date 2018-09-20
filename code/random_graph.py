##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Create a random conectivity matrix in which each edge is included with
## probability p (Erdos-Renyi model).

from numpy import random
import sys
from triangular import Triangular

# No. of nodes
N = 1024

#link probability
p = 1

#Link counter
lnkcnt = [0 for i in xrange(N)]

###Link matrix
##links = Triangular(N)

#link list
llinks = []

#make the links
for i in xrange(N-1):
    for j in range(i+1,N):
        pair = [min(i,j),max(i,j)]
        if random.random() < p:
            lnkcnt[i] += 1
            lnkcnt[j] += 1 
            #print(pair)
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

#f = open('connectivity.dat', 'w')
#for i in xrange(N):
#    for j in range(i+1,N):
#	f.write(str(links(i,j))+" ")
#    f.write("\n")
#f.close()
