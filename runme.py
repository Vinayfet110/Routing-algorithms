#!/usr/bin/env python
import numpy as np
from operator import itemgetter
#cmat=np.matrix([[daa,dab,dac,dad,dae,daf,dag,dah,dai,daj,dak],[dba,dbb,dbc,dbd,dbe,dbf,dbg,dbh,dbi,dbj,dbk]])
#cmat=np.matrix
inf=float('inf')
lis0=[]
lis1=[1,inf,1,inf,inf,inf,inf,inf,inf,inf]
lis2=[inf,1,inf,inf,inf,3,1,inf,inf,4]
lis3=[inf,inf,inf,inf,5,inf,inf,1,1,2]
lis4=[1,inf,inf,5,inf,inf,1,inf,inf,inf]
lis5=[inf,inf,3,inf,inf,inf,inf,inf,1,inf]
lis6=[inf,inf,1,inf,1,inf,inf,1,inf,inf]
lis7=[inf,inf,inf,1,inf,inf,1,inf,inf,inf]
lis8=[inf,inf,inf,1,inf,1,inf,inf,inf,inf]
lis9=[inf,inf,4,2,inf,inf,inf,inf,inf,inf]
cmat=np.array([lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8,lis9])

b=['a','b','c','d','e','f','g','h','i','j']
nodes=np.array([b,b,b,b,b,b,b,b,b,b])
print nodes.shape
ll=[0,inf,inf,inf,inf,inf,inf,inf,inf,inf]
print cmat.shape
node=np.array([b,b,b,b,b,b,b,b,b,b])
#span_tree=np.zeros((10,10))

dmat=np.array([ll,ll,ll,ll,ll,ll,ll,ll,ll,ll])
print dmat.shape
#i=0;j=0;ci=0;cj=0;di=0;dj=0
i=0;j=0;ci=0;cj=0;di=0;dj=0
#temp=[dmat[di,dj],dmat[di,dj+1],dmat[di,dj+2],dmat[di,dj+3],dmat[di,dj+4],dmat[di,dj+5],
#dmat[di,dj+6],dmat[di,dj+7],dmat[di,dj+8],dmat[di,dj+9]
#this for loop is for each hop and in each hop i calculated distance of all nodes to destination and incremented hops
for h in [1,2,3,4,5,6,7,8,9]:
	dmat[i+1,j]=0
	#j=j+1
	ind,dmat[i+1,j+1]=    min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
	dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
	dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
	dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	nodes[i+1,j+1]=node[ci,ind]
	ci=ci+1
	
	ind,dmat[i+1,j+2]=    min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))

	nodes[i+1,j+2]=node[ci,ind]
	
	ci=ci+1

	ind,dmat[i+1,j+3]=    min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	
	nodes[i+1,j+3]=node[ci,ind]
	ci=ci+1
	
	ind,dmat[i+1,j+4]=     min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	
	nodes[i+1,j+4]=node[ci,ind]
	ci=ci+1

	ind,dmat[i+1,j+5]=     min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	
	nodes[i+1,j+5]=node[ci,ind]

	ci=ci+1
	
	
	ind,dmat[i+1,j+6]=      min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	nodes[i+1,j+6]=node[ci,ind]

	ci=ci+1

	ind,dmat[i+1,j+7]=	    min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	nodes[i+1,j+7]=node[ci,ind]

	ci=ci+1

	ind,dmat[i+1,j+8]=      min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	nodes[i+1,j+8]=node[ci,ind]
	ci=ci+1


	ind,dmat[i+1,j+9]=      min(enumerate([cmat[ci,cj]+dmat[di,dj],cmat[ci,cj+1]+
        dmat[di,dj+1],cmat[ci,cj+2]+dmat[di,dj+2],cmat[ci,cj+3]+dmat[di,dj+3],cmat[ci,cj+4]+
        dmat[di,dj+4],cmat[ci,cj+5]+dmat[di,dj+5],cmat[ci,cj+6]+dmat[di,dj+6],cmat[ci,cj+7]+
        dmat[di,dj+7],cmat[ci,cj+8]+dmat[di,dj+8],cmat[ci,cj+9]+dmat[di,dj+9]]),key=itemgetter(1))
	
	nodes[i+1,j+9]=node[ci,ind]
	i=i+1
	di=di+1
	ci=0
for u in [1,2,3,4,5,6,7,8,9]:
	nodes[0,u]='-'
	nodes[1,2]='-'
	nodes[1,3]='-'
	nodes[1,5]='-'
	nodes[2,5]='-'
	nodes[1,6]='-'
	nodes[1,7]='-'
	nodes[2,7]='-'
	nodes[1:3,8]='-'
	nodes[1:3,9]='-'
print "The distances of each node to destination node in each hops 0,1,2--9 are as follows "	
print "The coloumns represent nodes"
print "The rows represent hops"
print "A0 B0 -- J0\nA1 B1 -- J1\nA2 B2 -- J2"
print dmat
print "\nThis matrix represents nodes i.e. coloums represent nodes and rows represent hops"
print node
print "\nThis matrix represents corresponding next node in the shortest path from a partricular node to destination "
print nodes

#cmat1=cmat.reshape(9,10)
#print cmat1.shape


