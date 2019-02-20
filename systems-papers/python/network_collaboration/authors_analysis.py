"""

Creates network of author collaboration.

- Nodes are authors.
- Nodes are linked if the authors collaborated on at
  least one paper in the data set.

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
from authors_network.authors_network import AuthorsNetwork

################################################################################
print("[*] Loading Data")

papers = s2data.get_dict_gA()

################################################################################
print("[*] Creating Authors Network")

G = AuthorsNetwork()
for paper_id, paper in papers.items(): G.add_paper(paper)
G.fill_graph()

################################################################################
if False:
  print("[*] Analyzing Network Statistics")
  G.print_statistics()

if False:
  print("[*] Calculating Network Centralities")
  G.calculate_centralities()

################################################################################
if False:
  print("[*] Analyzing Network")
  G.plot_centralities()

################################################################################
if False:
  print("[*] Writing Network File")
  G.write()

if True:
  print("[*] Coloring Nodes by CC-Size")
  G.fill_ccsizes()

################################################################################
if True:
  print("[*] Writing Network File")
  G.write()
