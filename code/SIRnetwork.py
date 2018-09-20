##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Three possible states: Susceptible(0), Infected(1), and Resistant(R)
## Every step, a number of edges is created conecting pairs of random individuals
## within the population. Whenever an infected node is conected to a
## susceptible node, the last one turns to infected with prob. "b".
## An infected can become resistant each step with prob. "g"
from numpy import random
import sys
from triangular import Triangular


#Number of steps
Nsteps = 200

#Number of nodes
N = 1000

#Fraction of initial infected nodes
ifr = 0.3

#Link frequency
bf = 5000 #links per step

#Infection probability
b = 0.3 / (2*bf/N)

#Prob. of becoming resistant
g = 0.1

#initial quantities
I = int(ifr*N)
S = N - I
R = 0

#Initialize nodes
nodes = [0 for i in range(N)]
count = I
while count > 0:
    rnd = random.randint(N)
    if nodes[rnd] == 0:
        nodes[rnd] = 1
        count -= 1
#print(nodes)

#initialize edges
edges = Triangular(N)
#edges.set_element(N-2,N-1,1)
#print(str(edges(N-2,N-1)))
#edges.set_zero()
#print(str(edges(N-2,N-1)))

f = open('sir_n.dat', 'w')

for n in xrange(Nsteps):
    f.write(str(n)+" "+str(S)+" "+str(I)+" "+str(R)+"\n")
  
    edges.set_zero()

    for i in xrange(bf):
	rnd1 = 0
	rnd2 = 0
	test = True
	
	while test:
	    rnd1 = random.randint(N)
	    rnd2 = random.randint(N)
	    
	    if rnd1 > rnd2:
		if edges(rnd2,rnd1) == 0:
		    edges.set_element(rnd2,rnd1,1)
		    test = False
	    elif rnd2 > rnd1:
		if edges(rnd1,rnd2) == 0:
		    edges.set_element(rnd1,rnd2,1)
		    test = False
	  
##	print(str(rnd1)+" "+str(rnd2))
	if (nodes[rnd2] == 1) and (nodes[rnd1] == 0):
	    if random.random() < b:
		nodes[rnd1] = 1 #gets infected
	elif (nodes[rnd1] == 1) and (nodes[rnd2] == 0):
	    if random.random() < b:
		nodes[rnd2] = 1 #gets infected

    # inmunoresistance
    for i in xrange(N):
	if (nodes[i] == 1) and (random.random() < g):
	    nodes[i] = 2
	    
    #Current compartment values
    S = 0
    I = 0
    R = 0
    for i in xrange(N):
	if nodes[i] == 0:
	    S += 1
	elif nodes[i] == 1:
	    I += 1
	elif nodes[i] == 2:
	    R += 1
	    
    if S+I+R != N:
	print("Problem with the conservation of nodes!")

f.close()
