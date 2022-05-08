import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


G = nx.Graph()
G = nx.read_edgelist('107.edges')
#网络中无 0 节点
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
L = np.loadtxt("107.egofeat")
print(len(L))




pos = nx.spring_layout(G)
nx.draw(G, node_color = 'blue', node_size = 10, width = 0.2 , with_labels=False, font_weight='bold' )
nx.draw_networkx_nodes(G, pos, nodelist = ['1888','1663','1833','1589','1584'], cmap=plt.get_cmap('jet'), node_color='orange', node_size=10, label=True, node_shape='o')
plt.savefig("./107graph.jpg")
plt.show()
