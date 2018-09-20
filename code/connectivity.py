##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------

## Create a conectivity matrix in which each edge is included with probability
## p (Erdös-Rényi model).

from numpy import random
import sys
from triangular import Triangular

# No. of nodes
N = 500

mu = 0.01 * N
sigma = 0.2 * mu

#Link number and counter
nlnks = [0 for i in xrange(N)]
lnkcnt = [0 for i in xrange(N)]

###Link matrix
##links = Triangular(N)
#link list
llinks = []

#No of links for each node
for i in xrange(N):
    nlk = int(random.normal(mu,sigma)) 
    if nlk >= N-1:
	nlk = N-2
    elif nlk < 0:
	nlk = 0
    nlnks[i] = nlk

#make the links
for i in xrange(N-1):
    dif = nlnks[i] - lnkcnt[i]
    if dif < 0:
	dif = 0
    for n in xrange(dif):
	rnd = i + 1 + random.randint(N-1-i)
	if random.random() >= 0.5:
	    lnkcnt[i] += 1
	    lnkcnt[rnd] += 1 
#	    print(str(i)+" "+str(rnd)+"\n")
#	    links.set_element(i,rnd,1)
	    pair = [i,rnd]
	    llinks.append(pair)
	else:
	    dif2 = nlnks[rnd] - lnkcnt[rnd]
	    if dif2 > 0:
		lnkcnt[i] += 1
		lnkcnt[rnd] += 1 
#	    	print(str(i)+" "+str(rnd)+"\n")
#	    	links.set_element(i,rnd,1)
		pair = [i,rnd]
		llinks.append(pair)

print(nlnks)
print(lnkcnt)

ff = open('connlist.dat', 'w')
for i in xrange(len(llinks)):
    ff.write(str(llinks[i][0])+" "+str(llinks[i][1])+"\n")
ff.close()

#f = open('connectivity.dat', 'w')
#for i in xrange(N):
#    for j in range(i+1,N):
#	f.write(str(links(i,j))+" ")
#    f.write("\n")
#f.close()
