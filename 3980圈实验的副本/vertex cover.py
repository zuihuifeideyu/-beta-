import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


f = '3980.edges'
#fn = open(f, 'r')
edges = np.loadtxt(f)
L_edges = edges.tolist()
#print(L_edges)
l = L_edges
#print(l[0])
vertex = []
i = 0
#del l[i]
#print(l[0])



for i in range(len(L_edges)):
    if not l:
        break
    else:
        l1 = l[0]
        #print(l1)
        vertex.append(l1[0])
        vertex.append(l1[1])
        j = 0
        while j < len(l):
            #print(l[j][0])
            #print(len(l))
            a = l[j][0]
            b = l[j][1]
            if (a == l1[0]) or (b == l1[0]) or (a == l1[1]) or (b == l1[1]):
                del l[j]
            else:
                j = j + 1
            #print(l[j][1])

#print(vertex)
t = [4030,4023,3998,3982,3997,4021,4014,4009,3994,4031]
n = 0
for i in range(len(t)):
    if t[i] in vertex:
        n = n+1

print(n)
print(len(vertex))
