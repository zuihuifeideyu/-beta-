import networkx as nx
import matplotlib.pyplot as plt
import random
import operator

G = nx.Graph()
G = nx.read_edgelist('1684.edges')
nx.draw(G, with_labels=True, node_color="red")
#plt.savefig("./graph.jpg")
plt.show()

pr = nx.pagerank(G, max_iter=100, alpha=0.01)  # 得到的是字典

print("最大PR值对应的节点：", max(pr.items(), key=operator.itemgetter(1))[0])
print("100个节点的PR值为：", pr)
pr2 = sorted(pr.items(),  key=lambda d: d[1], reverse=1)
print(pr2)


#前十个2863,3077,171,2951,3256,2724,2730,3136,3263,3019 0个
#greedy,
#2839,3363,3101,2754,2944,2966,2742,3320,3397,3291