import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


G = nx.Graph()
G = nx.read_edgelist('348.edges')

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
L = np.loadtxt("348.egofeat")
print(len(L))




pos = nx.spring_layout(G)
nx.draw(G, pos, node_color = 'blue', node_size = 10, width = 0.2 , with_labels=False, font_weight='bold' )
nx.draw_networkx_nodes(G, pos, nodelist = ['376','475','559','373','517'], cmap=plt.get_cmap('jet'), node_color='orange', node_size=10, label=True, node_shape='o')
plt.savefig("./348graph.jpg")
plt.show()
