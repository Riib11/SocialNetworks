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
from utils.debug import *
import utils.shared_utils as utils
import utils.combinatorics as u_combos
from tqdm import tqdm

# modules
import utils.data as u_data
import authors.author_features as a_features
import semantic_scholar.s2data as s2data
from authors_network.authors_network import AuthorsNetwork

################################################################################
message("Loading Data")

papers = s2data.get_dict_gA()

################################################################################
message("Creating Authors Network")

G = AuthorsNetwork()
for paper_id, paper in papers.items(): G.add_paper(paper)
G.fill_graph()

################################################################################
if False:
  message("Analyzing Network Statistics")
  G.print_statistics()

if True:
  message("Analyzing Centralities Correlations")
  G.print_centralities_correlations()

if False:
  message("Calculating All Network Centralities")
  G.calculate_centralities()

################################################################################
if False:
  message("Analyzing Network")
  G.plot_centralities()

elif False:
  cc_rank = 0
  message("Isolating the "+str(cc_rank)+"th Connected Component")
  G.isolate_component(cc_rank)

  if False:
    message("Calculating Nodes with All Centralities")
    G.calculate_centralities()

  if False:
    G.plot_component_centralities()

  if False:
    message("Filling Ndes with All Centralities")
    G.fill_all_centralities()

################################################################################

if False:
  message("Coloring Nodes by CC-Size")
  G.fill_ccsizes()

if False:
  centrality = "degree"
  message("Calculating Nodes' " + centrality + " Centrality")
  G.fill_centralities(centrality)

################################################################################
if False:
  message("Writing Network File")
  G.write()
