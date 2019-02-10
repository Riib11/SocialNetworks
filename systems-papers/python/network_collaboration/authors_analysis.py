"""

Creates a colored network of author collaboration.

- Info:

    - Nodes are identified by the respective author's names.

    - Edges are identified by the key of the paper that it represents collaboration on, with an 
      integer suffix to distinguish the many edges resulting from one paper collaboration. For 
      example, a paper with three authors results in three edges, since each author collaborated 
      with each other author once.

    - Coloring:
        - Color: Interpolates between Red and Blue, where Red is high and Blue is low (normalized for data set).
        - Node: Colored by the `hindex` of the author that the node reprents. Is that max of all values found among data/authors/*.json. If the target attribtute is not avaliable for a node, the node is colored black.
        - Edge: Colored by the maximum value of the nodes connected by this edge.

"""

# utilities
import sys
import os
import json
import numpy as np
import utils.conf_utils as conf_utils
import utils.shared_utils as utils
import utils.combinatorics as u_combos
from tqdm import tqdm

# modules
import utils.data as u_data
import authors.author_features as a_features
import semantic_scholar.s2data as s2data
from graph.papers_graph import AuthorsGraph

################################################################
print("[*] Loading Data")

papers = s2data.get_dict_gA()

################################################################
print("[*] Creating Authors Graph")

G = AuthorsGraph()
for paper_id, paper in papers.items(): G.add_paper(paper)
G.fill_graph()

################################################################
print("[*] Analyzing Graph")

G.print_statistics()

# G.calculate_centralities()
G.plot_centralities()

################################################################
print("[*] Writing Graph")

# G.write()
