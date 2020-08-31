"""
The folowwing is the code part of the canonicalization function.
The aim of this function to to compute and extract the canonical form of an
input graph that would be used later on in the Algorithm 4 of normalization

__version__ = 0.1
__author__ == 'Sofiane ENNADIR'

"""


import networkx as nx
from networkx import convert_node_labels_to_integers
from networkx import set_node_attributes as node_set

from pynauty.graph import canonical_labeling
from pynauty.graph import Graph

from labling_ranking_functions import *

def algorithm_of_cano(input_graph):
    """
        This function aims to compute the canonicalization step, where we want
        to extract of a certain graph its canonical correspondant.

        ---
        input:
            input_graph : A NetworkX instance which is our graph.
            node : The node for which we want to compute the function

    """

    # Let's transform the labels to an integer format so they can be used
    local_labeled_graph = convert_node_labels_to_integers(input_graph)
    labeled_graph = nx.Graph(local_labeled_graph)

    # Now, let's use the nauty package
    resulting_graph = Graph(len(local_labeled_graph.nodes()),directed=False)
    resulting_graph.set_adjacency_dict({n:list(nbrdict) for n,nbrdict in \
                                            local_labeled_graph.adjacency()})

    labels_dict=nx.get_node_attributes(local_labeled_graph,'labeling')
    canonical_labeling_dict={k:canonical_labeling(resulting_graph)[k] for k in \
                                        range(len(local_labeled_graph.nodes()))}

    # Ordering part
    comput_order = ranking_label(local_labeled_graph,labels_dict, \
                                                    canonical_labeling_dict)
    node_set(labeled_graph, comput_order, 'labeling')

    return labeled_graph
