##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


## Three possible states: Susceptible(0), Infected(1), and Resistant(R)
## Every step, a number of edges is created conecting pairs of random 
## individuals that are "adjacent" in the network.
## Adjacent nodes are determined by a conectivity matrix with some 
## distribution in the number of links a particular node has.
## Whenever an infected node is conected to a
## susceptible node, the last one turns to infected with prob. "b".
## An infected can be removed each step with prob. "g"
from numpy import random
import sys

#individuals**********************************************
class Unit:
    def __init__(self, i):
	self.iden = i
	self.state = 0
	self.neighbors = []
	
    def set_state(self, s):
	self.state = s
	
    def get_state(self):
	return self.state
	
    def add_neighbor(self, i):
	self.neighbors.append(i)
 
    def del_neighbor(self, i):
	ind = i - len(self.neighbors)
	try:
	    assert ind < 0 and i < N 
	except AssertionError:
            print("Index del_neighbor out of range.")
            return
	del self.neighbors[ind]
	
    def get_neighbors(self):
	return self.neighbors



#*********************************************************





def main():

  #Number of steps
  Nsteps = 200

  #Number of nodes
  N = 1024

  #Fraction of initial infected nodes
  ifr = 0.3

  #Infection probability
  b = 0.3/(1024)

  #Prob. of beeing removed
  g = 0.1


  #initial quantities
  I = int(ifr*N)
  S = N - I
  R = 0

  #Initialize nodes
  nodes = []
  for i in xrange(N):
      u = Unit(i)
      nodes.append(u)

  #Set initially infected
  count = I
  while count > 0:
      rnd = random.randint(N)
      if nodes[rnd].get_state() == 0:
	  nodes[rnd].set_state(1)
	  count -= 1
  #nodes[5050].set_state(1)
    
  #Load conectivity list
  with open('connlist.dat', 'r') as f_in: #This ensures that the file is closed, even in case of exeption
      for line in f_in:
	  pair = map(int, line.split())
	  nodes[pair[0]].add_neighbor(pair[1])
	  nodes[pair[1]].add_neighbor(pair[0])
  f_in.close()
  #for i in xrange(len(clist)):
  #    print(clist[i])

  f = open('random.dat', 'w')

  for n in xrange(Nsteps):
      #Print snapshot
      name = 'snapshots/snapshot_'+str(n)+'.dat'
      f_ss = open(name,'w')
      for unit in nodes:
	  f_ss.write('%s ' % unit.get_state())
      f_ss.close()
    
      f.write(str(n)+" "+str(S)+" "+str(I)+" "+str(R)+"\n")

      #infection
      for i in xrange(N):
	  if nodes[i].get_state() == 1:
	      ne = nodes[i].get_neighbors()
	      rnd = 0
	      if len(ne) > 0:
#		  rnd = random.randint(len(ne))
                  for n in xrange(len(ne)):
                      j = ne[n]
                      if nodes[j].get_state() == 0:
                          if random.random() < b:
                              #print nodes[j].get_state()
                              nodes[j].set_state(1) # gets infected
                              #print nodes[j].get_state()

      #removal
      for i in xrange(N):
	  if nodes[i].get_state() == 1:
	      if random.random() < g:
		  nodes[i].set_state(2)

      #Current compartment values
      S = 0
      I = 0
      R = 0
      for i in xrange(N):
	  if nodes[i].get_state() == 0:
	      S += 1
	  elif nodes[i].get_state() == 1:
	      I += 1
	  elif nodes[i].get_state() == 2:
	      R += 1
	    
      if S+I+R != N:
	  print("Problem with the conservation of nodes!")

  f.close()
##***************************************************************

main()
