##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Create a regular conectivity matrix in which each edge has the same number
## of links (same degree) connected to random nodes.

from numpy import random
import sys
from triangular import Triangular


def bridge(i, llinks, lnkcnt):
    test = False
    while not test:
        rnd = random.randint(0,len(llinks))
        a = llinks[rnd][0]
        b = llinks[rnd][1] 
        pair1 = [min(i,a),max(i,a)]
        pair2 = [min(i,b),max(i,b)]
        if ((a != i) and (b != i)) and ((pair1 not in llinks) and (pair2 not in llinks)):
            llinks.remove([a,b]) #remove a bond
            llinks.append(pair1) #add two new bonds
            llinks.append(pair2)
            lnkcnt[i] += 2
            test = True


# No. of nodes
N = 1024

# Connectivity degree of the network
deg = 128

# Max number of links
ml = N*(N-1)/2

# Theoretical number of links
tl = N*deg/2

#Link counter
lnkcnt = [0 for i in xrange(N)]

###Link matrix
##links = Triangular(N)

#link list
llinks = []

#Node list
nodes = [i for i in xrange(N)]

if (tl <= ml):
    count = 0
    while len(nodes) > 0:
        rnd1 = random.randint(0,len(nodes))
        rnd2 = random.randint(0,len(nodes))
        i = nodes[rnd1]
        j = nodes[rnd2]
        if i != j:
            ##
            #print('.')
            ##
            if (lnkcnt[i] < deg) and (lnkcnt[j] < deg):
                pair = [min(i,j),max(i,j)]
                ##
                #print(len(nodes),pair,rnd1,rnd2)
                ##
                if pair not in llinks:
                    count = 0

                    lnkcnt[i] += 1
                    lnkcnt[j] += 1
                
                    llinks.append(pair)
                    if lnkcnt[i] == deg: nodes.remove(i)
                    if lnkcnt[j] == deg: nodes.remove(j)
                    ##
                    #print(len(nodes))
                    ##
                else:
                    count += 1
                
            if count > len(nodes)*len(nodes):
                #verify all links between the remainder nodes are in the list 
                count1 = 0
                for n in range(0,len(nodes)-1):
                    a = nodes[n]
                    for m in range(n+1,len(nodes)):
                        b = nodes[m] 
                        pairv = [min(a,b),max(a,b)]
                        if pairv in llinks: count1 += 1
                tot = len(nodes)*(len(nodes)-1)/2
                ##
                #print(count,count1,tot)
                ##
                if count1 == tot:
                    if lnkcnt[i] < deg-1: #make a bridge
                        bridge(i,llinks,lnkcnt)
                    else:
                        nodes.remove(i)
                        
                    if lnkcnt[j] < deg-1: #make a bridge
                        bridge(j,llinks,lnkcnt)
                    else:
                        nodes.remove(j)
                    ##
                    #print(nodes)
                    ##

        elif len(nodes) == 1: 
            last = nodes[0]
            ##
            #print('last='+str(last))
            ##
            if lnkcnt[last] < deg-1: #make a bridge
                bridge(last,llinks,lnkcnt)
            else:
                nodes.remove(last)
                
        ##
        #print(lnkcnt)
        #print(nodes)
        ##
    print(lnkcnt)

    #print(len(llinks))
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

else:
    print('The connectivity degree is too high')
