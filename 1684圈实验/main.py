import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


G = nx.Graph()
G = nx.read_edgelist('1684.edges')
#网络中无 0 节点
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
L = np.loadtxt("1684.egofeat")
print(len(L))




pos = nx.spring_layout(G)
nx.draw(G, pos, node_color = 'blue', node_size = 10, width = 0.2 , with_labels=False, font_weight='bold' )
nx.draw_networkx_nodes(G, pos, nodelist = ['2839','3363','3101','2944','2754'], cmap=plt.get_cmap('jet'), node_color='orange', node_size=10, label=True, node_shape='o')
plt.savefig("./1684graph.jpg")
plt.show()
