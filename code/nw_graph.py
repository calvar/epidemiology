##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


"""Load links"""
def l_load():
    links = []
    with open('connlist.dat', 'r') as f_in: #This ensures that the file is closed, even in case of exeption
	for line in f_in:
	    pair = map(int, line.split())
	    links.append(pair)
    f_in.close()
    return links

"""Load nodes"""
def n_load(num):
    nodes = []
    name = 'snapshots/snapshot_'+str(num)+'.dat'
    with open(name,'r') as f_nd:
	for line in f_nd:
	    nodes = map(int,line.split())
    f_nd.close()
    return nodes

"""Define positions"""
def pos_def(side,nodes):
    pos = []
    indx = 0
    for i in range(side):
	for j in range(side):
	    c = 'b'
	    if nodes[indx] == 1:
		c = 'r'
	    elif nodes[indx] == 2:
		c = 'w'
	    dot = [i,j,c]
	    pos.append(dot)
	    indx += 1 
    return pos

"""plot a frame"""
def frame(nlinks,links,t):
    nodes = n_load(t)
    size = len(nodes)
    side = int(np.sqrt(float(size)))
    #print nodes
    
    pos = pos_def(side,nodes)
    #print pos

    """plot links"""
    for i in range(nlinks):
	n0 = links[i][0]
	n1 = links[i][1]
#    	print n0,n1
#    	print pos[n0],pos[n1]
	plt.plot([pos[n0][0],pos[n1][0]],[pos[n0][1],pos[n1][1]],linestyle='-',linewidth=0.5,color='g')
    """plot nodes"""
    for i in range(size):
	plt.plot([pos[i][0]],[pos[i][1]],marker='o',markersize=4,color=pos[i][2])
    plt.xlim([-1,side])
    plt.ylim([-1,side])

"""main function"""
def main():
    links = l_load()
    nlinks = len(links)
    #print links
    
    for t in range(20):
	print t
	plt.figure(figsize=(10,10), dpi=100)
	frame(nlinks,links,t)
	name = 'snapshots/snapshot_'+'{0:0>3}'.format(t)+'.png'
	plt.savefig(name)
	#plt.show()
    
##***********************************************************

main()
