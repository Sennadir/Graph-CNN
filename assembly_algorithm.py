"""
The folowwing is the main code implementation of the Assembly and Selection node
algorithm (Algorithm 1 and 2 in the paper.)

__version__ = 0.1
__author__ == 'Sofiane ENNADIR'


__remarks__ :
    * I should add the second part where we should append a dummy variable in
    the case where there isn't enough nodes to be added to the neighborhood.

"""

import networkx as nx

from labling_ranking_functions import *
from canonicalization import *
from normalization import *



def generate_nodes(graph, w, k, s, dict_label):

    """
        This function represents the implementation of Algorithm 1 in the paper
        where we select nodes and generate neighborhoods.

        We recall that in this part, we will be calling :
            * Sort nodes based on our labeling method
            * For each node, generate a receptive field
            * Pass to the other node respecting a stride parameter s

        ---
        input:
            input_graph : A NetworkX instance which is our graph.
            w : The width parameter
            k : The neighborhood size parameter
            s : the stride parameter

    """

    # Let's first sort our nodes in respect of our labeling function
    list_of_sorted_nodes = dict_label['main_order_of_nodes']

    graphlets = []

    index_node = 0
    index_width = 1

    while index_width <= w:

        # First case where we have enough nodes
        if index_node<len(list_of_sorted_nodes):
            graphlets.append(Create_The_receptive_field(graph,\
                                        list_of_sorted_nodes[index_node], k))

        # Second case where we don't have enough nodes (To be added)
        else:
            pass

        # Increase stride and width
        index_node = index_node + s
        index_width = index_width + 1

    return graphlets


def Create_The_receptive_field(input_graph,node, k):

    """
        This function represents the implementation of the creation of the
        receptive field.

        We recall that in this part, we will be calling :
            * Generate a neighborhood
            * Normalize the neighborhood using the normalization algorithm

        ---
        input:
            input_graph : A NetworkX instance which is our graph.
            node : The node for which we want to compute the function
            k : the neighborhood parameter

    """

    # Let's first select the neighbors
    neighbors = neighborhood_assembly_algorithm(input_graph,node, k)

    # Let's noralize the neighborhood
    resulting_neighborhood = normalization_algorithm(neighbors,node, k)

    return resulting_neighborhood

def neighborhood_assembly_algorithm(input_graph,node, k):
    """
        This function is an implementation of the Algorithm 2 of the paper where
        it's the neigboorhood assembly algorithm.

        Algorithm 2 to assembles a local neighborhood for the input node.

        ---
        input:
            input_graph : A NetworkX instance which is our graph.
            node : The node for which we want to compute
            k : The neighborhood size parameter
    """

    # Initiate our L and N
    first_set_of_nodes = {node} ## Defined in the paper as N
    second_set_of_nodes={node} ## Defined in the paper as L

    ## Add element to the set of nodes

    while len(first_set_of_nodes)<k and len(second_set_of_nodes)>0:
        temporary_set = set()

        for node_element in second_set_of_nodes:
            # Execute the union part of the algorith (L = Union(N_1(v)))
            temporary_set = \
                    temporary_set.union(set(input_graph.neighbors(node_element)))

        # Keep only the unique values in the temporary set
        second_set_of_nodes=temporary_set-first_set_of_nodes

        # Add the elements to the first set of nodes
        first_set_of_nodes = first_set_of_nodes.union(second_set_of_nodes)
        list_of_nodes = list(first_set_of_nodes)

        # Our final set assembled
        final_elements = input_graph.subgraph(list_of_nodes)

    return final_elements
