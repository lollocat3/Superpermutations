import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random
from termcolor import colored
def superpermutation(array, weights):
    final_string = ''
    l = len(array[0])
    for k in range(0, l):
        final_string+= str(array[0][k])
    for s in range(1, len(array)):
        el = array[s]
        ww = len(el)-weights[s-1]
        for g in range(ww, l):
            ch = str(el[g])
            final_string+=ch
    if l == 6:
        real_string = 'length: '+str(len(final_string)-1)+ ' --> '+ final_string
    else:
        real_string = 'length: '+str(len(final_string))+ ' --> '+ final_string
    return real_string

def find_element_by_weight(element, w):
    el = element
    if w == len(element):
        print 'ERROR: cannot have weight equal to length of element'
        return element
    elif w > len(element):
        print 'ERROR: cannot have weight greater than length of element'
        return element
    elif w <= 0:
        print 'ERROR: cannot have negative weight'
        return element
    else:
        for x in range(0, w):
            el.append(el[w-1-x])
        for k in range(0, w):
            el.remove(el[0])
    return el
#print find_element_by_weight([3, 1, 2], 2)
#print find_element_by_weight([1, 2, 3], 3)
#print find_element_by_weight([1, 2, 3, 4], 2)



def find_weights(num_el):
    weights = [1]
    current_num_el = 2
    while current_num_el < num_el:
        current_num_el += 1
        weights = find_weights_for(current_num_el, weights)
    return weights

def find_weights_for(current_num_el, initial_weights):
    temp_weights = []
    final_weights = []
    for i in range(0, len(initial_weights)):
        temp_weights.append(initial_weights[i]+1)
    for x in range(0, len(temp_weights)):
        for k in range(0, current_num_el-1):
            final_weights.append(1)
        final_weights.append(temp_weights[x])
    for n in range(0, current_num_el-1):
        final_weights.append(1)
    return final_weights

#print find_weights(4)

def find_path(weight_list, start):
    path = []
    el = start
    end = list()
    for w in range(0, len(weight_list)):
        el_copy = el[:]
        el = find_element_by_weight(el, weight_list[w])
        path.append(el_copy)
        #print el
    for a in range(1, len(start)+1):
        end.append(a)
    end = end[::-1]
    path.append(end)
    return path



P = nx.DiGraph()
start = list(input('symbols: '))
weight_list = find_weights(len(start))
complete_path = find_path(weight_list, start)
for b in range(0, len(complete_path)):
    if b < len(complete_path)-1:
        P.add_edge(tuple(complete_path[b]), tuple(complete_path[b+1]), weight=weight_list[b])


print superpermutation(complete_path, weight_list)
pos = nx.circular_layout(P)
esmall=[(u,v) for (u,v,d) in P.edges(data=True) if d['weight'] == 1]
elarge=[(u,v) for (u,v,d) in P.edges(data=True) if d['weight'] == 2]
ehuge=[(u,v) for (u,v,d) in P.edges(data=True) if d['weight'] == 3]
egigant=[(u,v) for (u,v,d) in P.edges(data=True) if d['weight'] == 4]
egigantic=[(u,v) for (u,v,d) in P.edges(data=True) if d['weight'] == 5]
nx.draw_networkx_edges(P,pos,edgelist=esmall,
                    width=2, edge_color='green')
nx.draw_networkx_edges(P,pos,edgelist=elarge,
                    width=2, edge_color='red')
nx.draw_networkx_edges(P,pos,edgelist=ehuge,
                    width=2, edge_color='blue')
nx.draw_networkx_edges(P,pos,edgelist=egigant,
                    width=2, edge_color='yellow')
nx.draw_networkx_edges(P,pos,edgelist=egigantic,
                    width=2, edge_color='black')
labels = nx.draw_networkx_labels(P,pos,font_size=7, font_weight='bold')
graph_ = input('graph? ')
if graph_ == 1:
    nx.draw(P, pos, node_size=900, node_color='red')
    #plt.figure(1,figsize=(100,100))
    plt.show()
else:
    print ''
