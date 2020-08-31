"""
The folowwing is the main code implementation of the Normalization algorithm
(Algorithm 4) where we will need the previously implemented functions.
It also creates the receptive field.

__version__ = 0.1
__author__ == 'Sofiane ENNADIR'


__remarks__ :
    * I should add the second part where we should append a dummy variable in
    the case where there isn't enough nodes to be added to the neighborhood.

"""

import networkx as nx

from canonicalization import *
from labling_ranking_functions import *


def normalization_algorithm(input_graph,node, k):
    """
        This function represents the implementation of the fourth algorithm in
        the paper which is the normalization.

        We recall that in this part, we will be calling :
            * The labeling function
            * The ranking function
            * Constructing the subgraphs
            * Canonicalize the outputs

        ---
        input:
            subgraph : A NetworkX instance which is our graph.
            node : The node for which we want to compute the function
            k : the neighborhood parameter

    """

    # Let's start by computing the labeling function (labeling_procedure)
    labeled_input_graph = labeling_procedure(input_graph)['main_graph_labels']
    resulting_order = nx.get_node_attributes(labeled_input_graph ,'labeling')

    # Compute the ranking related to the labeling already established
    subgraph_computed_ranking = compute_ranking(input_graph,node, \
                                        resulting_order)

    # First case of the algorithm (If there are more nodes in the subgraphs than
    # our parameter k)
    if len(subgraph_computed_ranking.nodes())>k:

        get_attributes_from_graph = \
            dict(nx.get_node_attributes(subgraph_computed_ranking,'labeling'))

        # Sort based on the attributes
        list_of_ranked_nodes = sorted(get_attributes_from_graph,\
                                        key=get_attributes_from_graph.get)[0:k]

        # Compute the subgraph
        subgraph_with_ranking = \
                        subgraph_computed_ranking.subgraph(list_of_ranked_nodes)

        # Reuse the labeling procedure to get the main graph (we recall taht
        # the output of the function is a dictionnary)
        labeled_input_graph = labeling_procedure(input_graph)['main_graph_labels']
        resulting_order = nx.get_node_attributes(labeled_input_graph ,'labeling')
        subgraph_ranked_N = compute_ranking(subgraph_with_ranking,node, resulting_order)

    # Second case of the algorithm (If there are not more nodes in the subgraphs than
    # our parameter k)

    elif len(subgraph_computed_ranking.nodes()) < k:
        ## To be added : should add the other case
        pass

    return algorithm_of_cano(subgraph_ranked_N)
