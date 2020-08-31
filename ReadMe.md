# CNN for Graph

The following project is an implementation of the CNN for Graphs approach presented
in the paper "Learning Convolutional Neural Networks for Graphs".

## Requirement

The following packages are necessary to compute this code :
* NetworkX
* Matplotlib
* Pynauty (NAUTY)

## Usage

The code can be directly used using the following command :
* Start first by generating a graph

```python
G = nx.erdos_renyi_graph(100,0.15)
```
* Then you can compute the subgraphs by :

```python
l = generate_nodes(G, w, k, s, labeling_procedure(G))
```

You can directly find all of that in the main.py code.


## Remarks

* I didn't yet have the time to compute the CNN part, I only generate the subgraphs
that are labeled and ready to be used as we have the different receptive fields.
I will try to implement the CNN part very soon (any contribution in that part is welcomed).

* I didn't also add the part where the number of nodes are note enough to generate
the fields. I will try to add that later on.

* To have a more easy-implemented code, I will have to implement all that in a class.

* Be careful in the installation of the PyNauty package. In ideal, you should use
a virtual environment for this project. If you can't install it, I can send you my
environment.

Please let me know if you have any remarks or additions.

## Contact
Feel free to contact me by email or by LinkedIn. Feel free to use this code for
your different projects :).
