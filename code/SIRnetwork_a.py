##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Three possible states: Susceptible(0), Infected(1), and Resistant(R)
## Every step, every infected individual is tested against all susceptibles,
## (all nodes are connected) and infection occurs with probability b.
## An infected can become resistant each step with prob. "g"
from numpy import random
import sys
#from triangular import Triangular


#Number of steps
Nsteps = 200

#Number of nodes
N = 1024

#Fraction of initial infected nodes
ifr = 0.3

#Infection probability
b = 0.3/(N-1)

#Prob. of becoming resistant
g = 0.1

#initial quantities
I = int(ifr*N)
S = N - I
R = 0

#Initialize nodes: S (0) and I (1)
nodes = [0 for i in range(N)]
count = I
while count > 0:
    rnd = random.randint(N)
    if nodes[rnd] == 0:
        nodes[rnd] = 1
        count -= 1
#print(nodes)


f = open('sir_n.dat', 'w')

for n in xrange(Nsteps):
    f.write(str(n)+" "+str(S)+" "+str(I)+" "+str(R)+"\n")

    # infection
    for i in xrange(N):
	if nodes[i] == 1: #if infected
	    for j in xrange(N):
		if (j != i) and (nodes[j] == 0): # if susceptible
		    if random.random() < b:
			nodes[j] = 1
  
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
