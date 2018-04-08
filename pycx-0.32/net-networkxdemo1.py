# Meira Chefitrz HCI ABM

#relies on Sayam How to use NetworkX (1)


import random as RD
import pylab as PL
import scipy as SP
import networkx as nx
from networkx.algorithms import bipartite

RD.seed()

### creating networks

# manual construction



B = nx.Graph()
# Add the node attribute "bipartite" - Peceivers = 0
B.add_nodes_from([1,2,3,4, 5, 6], bipartite=0) 
# Add the node attribute "bipartite" - Targets = 1
B.add_nodes_from(['a','b','c', 'd','e', 'f', 'g', 'h', 'm', 'q'], bipartite=1)
B.add_edges_from([(1,'a'), (1,'e'), (1,'f'), (2,'b'), (2,'e'), (2,'g'), 
                  (3,'c'), (3,'e'), (3,'h'),(3,'g'),(4,'d'), (5, m), (6, q)])



g = NX.Graph()
g.add_edge(i, j)
#g.add_edge(2, 3)
#g.add_node(5)
g.remove_node(4)
g.remove_edge(1, 2)

# complete graph with 10 nodes
K10 = NX.complete_graph(10)

# from adjacency matrix
mat = NX.from_numpy_matrix(SP.array([[0,1,0,1,1],
                                     [1,0,0,1,0],
                                     [0,0,0,0,1],
                                     [1,1,0,0,0],
                                     [1,0,1,0,0]]))

### visualizing networks

PL.subplot(1, 3, 1)
NX.draw(g)
PL.axis('image')
PL.title('g')

PL.subplot(1, 3, 2)
NX.draw_circular(K10)
PL.axis('image')
PL.title('K10')

PL.subplot(1, 3, 3)
NX.draw_random(mat)
PL.axis('image')
PL.title('mat')

PL.draw()

### obtaining basic information about networks

print 'Number of nodes in K10 is', K10.number_of_nodes()

print 'List of nodes in K10:'
print K10.nodes()

print 'Number of edges in K10 is', K10.number_of_edges()

print 'List of edges in K10:'
print K10.edges()

print

print 'Adjacency matrix of K10 in NumPy array format:'
print NX.to_numpy_matrix(K10)

print

# connected components
cc = NX.connected_components(g)
print 'There are', len(cc), 'connected components in g'
print 'They are:'
print cc

print

# shortest paths and characteristic path lengths
print 'Shortest path from 1 to 4 in mat is:'
print NX.shortest_path(mat, 1, 4)
print 'whose length is', NX.shortest_path_length(mat, 1, 4)
print 'Diameter (maximum of shortest path lengths) of mat is', NX.diameter(mat)
print 'Average shortest path length of mat is', NX.average_shortest_path_length(mat)

print

# clustering coefficients
print 'Clustering coefficients of nodes in mat are:'
print NX.clustering(mat)
print 'whose average is', NX.average_clustering(mat)

print

# degrees and degree distribution
print 'Neighbors of node 0 in mat is:'
print mat.neighbors(0)
print 'Its degree is', mat.degree(0)

print

print 'Degrees of all nodes in mat are:'
print NX.degree(mat)

hist = NX.degree_histogram(mat)
print 'When binned:'
print hist
print 'See figure for its histogram'

PL.figure()
PL.plot(hist)
PL.xlabel('Degree (k)')
PL.ylabel('# of nodes (P(k))')
PL.title("Degree distribution of the network 'mat'")

print

# centralities
print 'Betweenness centralities of all nodes in mat are:'
print NX.betweenness_centrality(mat)
print 'Closeness centralities of all nodes in mat are:'
print NX.closeness_centrality(mat)
print 'Eigenvector centralities of all nodes in mat are:'
print NX.eigenvector_centrality(mat)

PL.show()
