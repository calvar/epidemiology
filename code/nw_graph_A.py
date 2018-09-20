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
def pos_def(side):
    pos = []
    for i in range(side):
	for j in range(side):
	    dot = [i,j]
	    pos.append(dot)
    return pos

"""define color"""
def color(nodes):
    col = []
    for i in nodes:
	c = 'b'
	if i == 1:
	    c = 'r'
	elif i == 2:
	    c = 'w'
	col.append(c)
    return col


"""plot a frame"""
def frame(nlinks,links,pos,t):
    nodes = n_load(t)
    size = len(nodes)
    side = int(np.sqrt(float(size)))
    #print nodes

    col = color(nodes)

    """plot links"""
    for i in range(nlinks):
	n0 = links[i][0]
	n1 = links[i][1]
#    	print n0,n1
#    	print pos[n0],pos[n1]
	plt.plot([pos[n0][0],pos[n1][0]],[pos[n0][1],pos[n1][1]],linestyle='-',linewidth=0.5,color='g')
    """plot nodes"""
    for i in range(size):
	plt.plot([pos[i][0]],[pos[i][1]],marker='o',markersize=4,color=col[i])
    plt.xlim([-1,side])
    plt.ylim([-1,side])

"""main function"""
def main():
    links = l_load()
    nlinks = len(links)
    #print links
    
    nodes = n_load(0)
    size = len(nodes)
    side = int(np.sqrt(float(size)))
    
    pos = pos_def(side)
    
    for t in range(1):
	print t
	plt.figure(figsize=(10,10), dpi=100)
	frame(nlinks,links,pos,t)
	name = 'snapshots/snapshot_'+'{0:0>3}'.format(t)+'.png'
	#plt.savefig(name)
	plt.show()
    
##***********************************************************

main()
