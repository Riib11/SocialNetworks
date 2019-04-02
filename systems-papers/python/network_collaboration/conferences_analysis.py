# utilities
import sys
import os
import json
import numpy as np
import utils.conf_utils as conf_utils
import utils.shared_utils as utils
import utils.combinatorics as u_combos
import utils.debug as debug
from tqdm import tqdm
import networkx as nx

# modules
import utils.data as u_data
import semantic_scholar.s2data as s2data
from conferences_network.conference_collaborations_network import ConfereneCollaborationNetwork

#############################################################################################################################
# Create
debug.message("Creating Conferences Network")

G = ConfereneCollaborationNetwork()
G.fill()

#############################################################################################################################
# Analysis
