"""
The folowwing is the first part of the implementation where we compute the
different labeling functions and ranking function. We mainly use the different
labeling function already impelemented in NetworkX (For example the betweenees
Algorithm).

__version__ = 0.1
__author__ == 'Sofiane ENNADIR'

"""

import networkx as nx
from networkx import single_source_dijkstra_path_length as dijkstra
from networkx import set_node_attributes as node_set

def labeling_procedure(input_graph):
    """
        The following function aims to compute the betweenees labeling

        ---
        Input:
            input_graph : A NetworkX instance which is our graph.

    """

    # Extract centrality based on betweeness (from the NetworkX package)
    centrality=list(nx.betweenness_centrality(input_graph).items())

    # Sort our centrality and compute a dict (Eeasier to work with)
    centrality.sort(key=lambda tup: tup[1], reverse=True)
    dict_graph = {centrality[i][0]: i for i in range(len(centrality))}


    # Label our graph in respect of the ordered centrality labeling already
    # computed
    node_set(input_graph, dict_graph, 'labeling')

    ordered_nodes=list(zip(*centrality))[0]

    dict_temp = {
    'main_graph_labels' : input_graph,
    'main_order_of_nodes' : list(zip(*centrality))[0]
    }

    return dict_temp


def dijkstra_labeling(input_graph,node):
    """
        This function is an utility one that aims to use the signe source Dijkstra
        path algorithm as a Labeling function

        ---
        input:
            input_graph : A NetworkX instance which is our graph.
            node : The node for which we want to compute the function

    """

    node_set(input_graph,dijkstra(input_graph, node),'labeling')
    return input_graph


def ranking_label(input_graph,label_dict,true_dict):

    """
        Given a certain labeling dictionnary (computed in the previous functions),
        the aim of the function is to respect

        ---
        input:
            input_graph : A NetworkX instance which is our graph.
            labeling_dictionnary : The node for which we want to compute the function

    """

    index_value=0

    for label in list(set(label_dict.values())):

        list_of_nodes = []
        for element_1, element_2 in input_graph.nodes(data = True):
            if element_2['labeling'] == label :
                list_of_nodes.append(element_1)

        if len(list_of_nodes) >= 2:
            dict_ordered = {sorted(list_of_nodes, key=true_dict.get)[i]: \
                i for i in range(len(sorted(list_of_nodes, key=true_dict.get)))}

            for index,value in dict_ordered.items():
                label_dict[index]= index_value + 1 + dict_ordered[index]
            index_value += len(list_of_nodes)

        else :
            label_dict[list_of_nodes[0]] = index_value + 1
            index_value += 1

    return label_dict

def compute_ranking(input_graph,node, resulting_order):

    """
        This function aims to compute the ranking of a certain input graph using
        the ranking functon already established.

        ---
        input:
            input_graph : A NetworkX instance which is our graph.
            node : The node for which we want to compute the function

    """

    output_graph = nx.Graph(input_graph)
    temp_order_graph = dijkstra_labeling(input_graph,node)

    input_labels = nx.get_node_attributes(temp_order_graph,'labeling')
    dictionnary_of_order = ranking_label(temp_order_graph,input_labels,\
                                                            resulting_order)
    node_set(output_graph,dictionnary_of_order,'labeling')

    return output_graph
