import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random

def find_weight(s1, s2, n):
    w = n
    dir = '<->'
    if n == 2:
        w = 1
    if n == 3:
        if str(s2[0])+str(s2[1]) == str(s1[n-2])+str(s1[n-1]):
            w = 1
            dir = '->'
        elif str(s2[0]) == str(s1[n-1]):
            w = 2
            dir = '->'
    if n == 4:
        if str(s2[0])+str(s2[1])+str(s2[2]) == str(s1[n-3])+str(s1[n-2])+str(s1[n-1]):
            w = 1
            dir = '->'
        elif  str(s2[0])+str(s2[1]) == str(s1[n-2])+str(s1[n-1]):
            w = 2
            dir = '->'
        elif  str(s2[0]) == str(s1[n-1]):
            w = 3
            dir = '->'
    if n == 5:
        if str(s1[n-4])+str(s1[n-3])+str(s1[n-2])+str(s1[n-1]) == str(s2[0])+str(s2[1])+str(s2[2])+str(s2[3]):
            w = 1
            dir = '->'
        elif str(s1[n-3])+str(s1[n-2])+str(s1[n-1]) == str(s2[0])+str(s2[1])+str(s2[2]):
            w = 2
            dir = '->'
        elif str(s1[n-2])+str(s1[n-1]) == str(s2[0])+str(s2[1]):
            w = 3
            dir = '->'
        elif str(s1[n-1]) == str(s2[0]):
            w = 4
            dir = '->'
    return w, dir



n = tuple(input("symbol tuple = "))






l = list(itertools.permutations(n))
G = nx.DiGraph()
#g = nx.DiGraph((x, y, {'weight': v})
edge_list = []
count = 1
for y in range(0, len(l)):
    for x in range(y+1,len(l)):
        #G.add_edges_from([(l[y], l[x], {'weight':find_weight(l[y], l[y], len(n))}),(l[x], l[y], {'width':0})])
        w1, dir1 = find_weight(l[y], l[x], len(n))
        print str(count) + ' ' + str(l[y]) + ' ' + str(l[x]) + ' ' + str(w1) + ' ' + dir1
        count = count + 1
        w2, dir2 = find_weight(l[x], l[y], len(n))
        print str(count) + ' ' + str(l[x]) + ' ' + str(l[y]) + ' ' + str(w2) + ' ' + dir2
        count=count + 1
        if w1 == 1:
            G.add_edge(l[y], l[x], weight=w1, arrowstyle=dir1)
        elif w2 == 1:
            G.add_edge(l[x], l[y], weight=w2, arrowstyle=dir2)
        elif w1 == len(n):
            print "waste (weight equals:) "+ str(len(n))
        elif w2 == len(n):
            print "waste (weight equals:) "+ str(len(n))
        elif w1 < w2:
            if w1 > 1 and w1 < len(l) and l[y][w1-1] == l[x][w1]:
                G.add_edge(l[y], l[x], weight=w1, arrowstyle=dir1)
                edge_list.append([l[y], l[x], w1])
            else:
                print 'waste (improper edge)'
        elif w1 > w2:
            if w2 > 1 and w2 < len(l) and l[x][w2-1] == l[y][w2]:
                G.add_edge(l[x], l[y], weight=w2, arrowstyle=dir2)
                edge_list.append([l[x], l[y], w2])
            else:
                print 'waste (improper edge)'
        else:
            G.add_edge(l[y], l[x], weight=w1, arrowstyle='<->')
            G.add_edge(l[x], l[y], weight=w2, arrowstyle='<->')
            edge_list.append([l[x], l[y], w2])
            edge_list.append([l[y], l[x], w1])

#print edge_list









pos = nx.circular_layout(G) # positions for all nodes
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == 1]
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == 2]
ehuge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == 3]
egigant=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == 4]
egigantic=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] == 5]




nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=2, edge_color='green')
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=2, edge_color='red')
nx.draw_networkx_edges(G,pos,edgelist=ehuge,
                    width=2, edge_color='blue')
nx.draw_networkx_edges(G,pos,edgelist=egigant,
                    width=2, edge_color='yellow')
nx.draw_networkx_edges(G,pos,edgelist=egigantic,
                    width=2, edge_color='black')





labels = nx.draw_networkx_labels(G,pos,font_size=6)
nx.draw(G, pos, node_size=1000)
#plt.savefig("graph_N=3")
plt.show()
