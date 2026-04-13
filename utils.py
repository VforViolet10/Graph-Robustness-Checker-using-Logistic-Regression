# utils.py

import pickle
import networkx as nx
import numpy as np


def load_graph_features(file_path):
    """
    Loads a graph from .pkl file and converts it into simple ML features.

    Returns:
        features (list): [num_nodes, num_edges, avg_degree]
        label (int): graph label (if present)
    """

    # Load graph
    with open(file_path, "rb") as f:
        G = pickle.load(f)

    # Number of nodes
    num_nodes = G.number_of_nodes()

    # Number of edges
    num_edges = G.number_of_edges()

    # Average degree = 2E / N
    avg_degree = (2 * num_edges) / num_nodes if num_nodes > 0 else 0

    features = [num_nodes, num_edges, avg_degree]

    # Get label (if exists)
    label = G.graph.get("target", None)

    return features, label
