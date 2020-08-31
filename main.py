"""
The folowwing is the main code to the implementation of the Paper.

__version__ = 0.1
__author__ == 'Sofiane ENNADIR'

"""

import networkx as nx
import matplotlib.pyplot as plt

from assembly_algorithm import generate_nodes
from labling_ranking_functions import labeling_procedure

# Define parameters
w = 100 # Width parameter
k = 6 # Number of elements in a neighborhood
s = 1 # Stride parameter


if __name__ == '__main__':
    # Let's generate a random graph (I will be using the erdos renyi graph)
    G = nx.erdos_renyi_graph(100,0.15)

    # In case you want to draw the graph use this
    nx.draw(G)

    # List of subgraphs
    l = generate_nodes(G, w, k, s, labeling_procedure(G))

    print(len(l))
