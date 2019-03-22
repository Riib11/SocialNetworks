"""

Creates network of papers, linked by shared authors.

- Nodes are papers.
- Nodes are linked if they share an author (disambiguated by Semantic Scholar id record).

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
from papers_network.papers_network import PapersNetwork

################################################################################
# Load Data
print("[*] Loading Data")

papers = s2data.get_dict_gA()
print()

################################################################################
# Initialization
print("[*] Creating Papers Network")

G = PapersNetwork()
G.add_papers(papers)
G.fill_graph()

################################################################################
# Analysis
if False:
  print("[*] Analyzing Network Statistics")
  G.print_statistics()

if False:
  print("[*] Calculating Network Centralities")
  G.calculate_centralities()

################################################################################
# Present Results
if False:
  print("[*] Preparing Results for Presentation")
  G.plot_centralities()

################################################################################
# Attributes
if False:
  centrality_name = "betweenness"
  print("[*] Coloring nodes by "+centrality_name+" centrality")
  G.fill_node_centralities(centrality_name)


################################################################################
# Write gexf
if True:
  print("[*] Writing Network File")
  G.write()
