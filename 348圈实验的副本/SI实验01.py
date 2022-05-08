import io
import random
import urllib.request as urllib
import zipfile
import time
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

'''
author：xiao黄
time：2020-9-26
'''

'''
1 易感人群（Susceptible）：指未得病者，但缺乏免疫能力，与感病者接触后容易受到感染。
2 感染人群（Infective）：指染上传染病的人，他可以传播给易感人群。
3 移除人群（Removed）：被移出系统的人。因病愈（具有免疫力）或死亡的人。这部分人不再参与感染和被感染过程。
N(t) = S(t) + I(t) + R(t)
S(t+1) = S(t) - αS(t)
I(t+1) = I(t) - βI(t)
R(t+1) =  R(t) + βI(t)
'''

max_iter_num = 10  # 模拟的次数

G = nx.read_edgelist('348.edges')

nums = G.number_of_nodes()  # 足球数据节点 -> 25
print('总节点数', nums)


ls1 = [376,475,373,559,517,497,483,412,513,428]
ls2 = [376,475,412,497,373,553,500,561,513,428]
ls3 = [563,549,198,412,373,419,428,376,463,437]
ls4 = [563,532,376,475,412,504,460,373,453,428]
ls5 = [376,475,412,563,428,373,497,513,561,525]

list1 = [str(i) for i in ls1]
list2 = [str(i) for i in ls2]
list3 = [str(i) for i in ls3]
list4 = [str(i) for i in ls4]
list5 = [str(i) for i in ls5]

'''
#紧密中心性对比
list3 = nx.closeness_centrality(G)
print(list3)

max_prices3 = max(zip(list3.values(), list3.keys()))
print(max_prices3[1])
'''



#SI实验
alpha = 0.1  # 传染概率
#beta = 0.65  # 治愈概率


#TS实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list1:
    G.nodes[node]['state'] = 1

all_infect_nodes1 = []  # 所有被感染的节点放在这里
for node in list1:
    all_infect_nodes1.append(node)

all_remove_nodes1 = []  # 所有被治愈的节点放在这里

infect1 = []  # 随着迭代次数的增加的感染总人数
recover1 = []  # 随着迭代次数的增加的治愈总人数



for i in range(max_iter_num):
    new_infect1 = list()  # 新被感染的
    new_remove1 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect1.append(len(all_infect_nodes1))
    recover1.append(len(all_remove_nodes1))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes1:

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                edge_data = G.get_edge_data(v, nbr)
                if alpha < edge_data['weight']:
                    G.nodes[nbr]['state'] = 1
                    new_infect1.append(nbr)

    for i in new_remove1:
        if i in new_infect1:
            new_infect1.remove(i)
        if i in all_infect_nodes1:
            all_infect_nodes1.remove(i)

    all_infect_nodes1.extend(new_infect1)  # 将新感染的添加到
    all_remove_nodes1.extend(new_remove1)
    all_infect_nodes1 = list(set(all_infect_nodes1))  # 去重
    all_remove_nodes1 = list(set(all_remove_nodes1))





#度中心性实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list2:
    G.nodes[node]['state'] = 1

all_infect_nodes2 = []  # 所有被感染的节点放在这里
for node in list2:
    all_infect_nodes2.append(node)

all_remove_nodes2 = []  # 所有被治愈的节点放在这里

infect2 = []  # 随着迭代次数的增加的感染总人数
recover2 = []  # 随着迭代次数的增加的治愈总人数

for i in range(max_iter_num):
    new_infect2 = list()  # 新被感染的
    new_remove2 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect2.append(len(all_infect_nodes2))
    recover2.append(len(all_remove_nodes2))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes2:

        for nbr in G.neighbors(v):  # v的邻居


            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                edge_data = G.get_edge_data(v, nbr)
                if alpha < edge_data['weight']:
                    G.nodes[nbr]['state'] = 1
                    new_infect2.append(nbr)

    for i in new_remove2:
        if i in new_infect2:
            new_infect2.remove(i)
        if i in all_infect_nodes2:
            all_infect_nodes2.remove(i)

    all_infect_nodes2.extend(new_infect2)  # 将新感染的添加到
    all_remove_nodes2.extend(new_remove2)
    all_infect_nodes2 = list(set(all_infect_nodes2))  # 去重
    all_remove_nodes2 = list(set(all_remove_nodes2))





# 介数中心性实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list3:
    G.nodes[node]['state'] = 1

all_infect_nodes3 = []  # 所有被感染的节点放在这里
for node in list3:
    all_infect_nodes3.append(node)

all_remove_nodes3 = []  # 所有被治愈的节点放在这里

infect3 = []  # 随着迭代次数的增加的感染总人数
recover3 = []  # 随着迭代次数的增加的治愈总人数



for i in range(max_iter_num):
    new_infect3 = list()  # 新被感染的
    new_remove3 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect3.append(len(all_infect_nodes3))
    recover3.append(len(all_remove_nodes3))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes3:

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                edge_data = G.get_edge_data(v, nbr)
                if alpha < edge_data['weight']:
                    G.nodes[nbr]['state'] = 1
                    new_infect3.append(nbr)

    for i in new_remove3:
        if i in new_infect3:
            new_infect3.remove(i)
        if i in all_infect_nodes3:
            all_infect_nodes3.remove(i)

    all_infect_nodes3.extend(new_infect3)  # 将新感染的添加到
    all_remove_nodes3.extend(new_remove3)
    all_infect_nodes3 = list(set(all_infect_nodes3))  # 去重
    all_remove_nodes3 = list(set(all_remove_nodes3))

##############################################################

# PG实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list4:
    G.nodes[node]['state'] = 1

all_infect_nodes4 = []  # 所有被感染的节点放在这里
for node in list4:
    all_infect_nodes4.append(node)

all_remove_nodes4 = []  # 所有被治愈的节点放在这里

infect4 = []  # 随着迭代次数的增加的感染总人数
recover4 = []  # 随着迭代次数的增加的治愈总人数


for i in range(max_iter_num):
    new_infect4 = list()  # 新被感染的
    new_remove4 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect4.append(len(all_infect_nodes4))
    recover4.append(len(all_remove_nodes4))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes4:

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                edge_data = G.get_edge_data(v, nbr)
                if alpha < edge_data['weight']:
                    G.nodes[nbr]['state'] = 1
                    new_infect4.append(nbr)

    for i in new_remove4:
        if i in new_infect4:
            new_infect4.remove(i)
        if i in all_infect_nodes4:
            all_infect_nodes4.remove(i)

    all_infect_nodes4.extend(new_infect4)  # 将新感染的添加到
    all_remove_nodes4.extend(new_remove4)
    all_infect_nodes4 = list(set(all_infect_nodes4))  # 去重
    all_remove_nodes4 = list(set(all_remove_nodes4))



# CC中心性实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list5:
    G.nodes[node]['state'] = 1

all_infect_nodes5 = []  # 所有被感染的节点放在这里
for node in list5:
    all_infect_nodes5.append(node)

all_remove_nodes5 = []  # 所有被治愈的节点放在这里

infect5 = []  # 随着迭代次数的增加的感染总人数
recover5 = []  # 随着迭代次数的增加的治愈总人数


for i in range(max_iter_num):
    new_infect5 = list()  # 新被感染的
    new_remove5 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect5.append(len(all_infect_nodes5))
    recover5.append(len(all_remove_nodes5))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes5:

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈
                edge_data = G.get_edge_data(v, nbr)
                if alpha < edge_data['weight']:
                    G.nodes[nbr]['state'] = 1
                    new_infect5.append(nbr)

    for i in new_remove5:
        if i in new_infect5:
            new_infect5.remove(i)
        if i in all_infect_nodes5:
            all_infect_nodes5.remove(i)

    all_infect_nodes5.extend(new_infect5)  # 将新感染的添加到
    all_remove_nodes5.extend(new_remove5)
    all_infect_nodes5 = list(set(all_infect_nodes5))  # 去重
    all_remove_nodes5 = list(set(all_remove_nodes5))


# matplotlib中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # aaaaa.py 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）


def draw_picture(nums, max_iter_num, infect1, recover1, infect2, recover2, infect3, recover3, infect4, recover4,
                 infect5, recover5):
    x = range(max_iter_num)
    susceptible = []
    #    for i in range(max_iter_num):
    #        susceptible.append(nums - infect1[i] - recover1[i])

    plt.figure(figsize=(5, 4), dpi=150)  # 图片大小，清晰度

    plt.plot(x, infect1, color='r', label='TS', lw=1, marker='s', linestyle='-')
    plt.plot(x, infect2, color='b', lw=1, marker='o', linestyle='--', label='DC')
    plt.plot(x, infect3, color='g', lw=1, marker='p', linestyle='-.', label='BC')
    plt.plot(x, infect4, color='y', lw=1, marker='h', linestyle='-.', label='PG')
    plt.plot(x, infect5, color='m', lw=1, marker='d', linestyle='-.', label='CC')

    #    plt.title('infections')
    # plt.plot(x, recover, color='b', label='治愈数')  # 可以修改颜色、线条风格、图例
    # plt.plot(x, susceptible, color='g', label='易感数')

    plt.legend(loc='lower right')  # 显示图例

    plt.xticks(range(0, max_iter_num, 2))  # 修改x的刻度
    plt.yticks(range(0, nums, 50))  # 修改y的刻度

    # 添加网格显示
    plt.grid(True, linestyle='', alpha=0.5)

    # 添加x，y轴描述信息及标题
    plt.ylabel('Infected nodes')
    plt.xlabel('Timestamps')

    #    # plt.title('对比')
    plt.savefig("./348对比graph.jpg")
    plt.show()



draw_picture(nums, max_iter_num, infect1, recover1, infect2, recover2, infect3, recover3, infect4, recover4, infect5,
             recover5)


