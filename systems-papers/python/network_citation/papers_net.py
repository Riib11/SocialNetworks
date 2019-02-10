"""

Creates a network of conference citations.

- Info:

    - Nodes represent a conference
    - Edges are directed and one weight point represents one paper in a conference citing another paper in another conference

"""

# utilities
import sys
import os
import numpy as np
import utils.shared_utils as utils
import utils.conf_utils as conf_utils
import utils.colors as u_colors
import utils.combinatorics as u_combos
from tqdm import tqdm

# modules
from net.net import NET
import utils.data as u_data
import semantic_scholar.s2data as s2data

################################################################
print("[#] Initializing NET")

# graph init
graph = NET("citations_papers")

################################################################
print("[#] Loading Data:")

gA = s2data.get_dict_gA()
gB = s2data.get_dict_gB()

################################################################
print("[#] Analyzing Data:")

nodes = []

for id, paper in gA.items():
    if len(paper["venue"]) == 0: continue
    nodes.append(id)
    for target_id in paper["outCitations"]:
        nodes.append(target_id)

# remove duplicates
nodes = list(set(nodes))

# add all nodes
for node in nodes: graph.addNode(node)

# add all edges
for id, paper in gA.items():
    if len(paper["venue"]) == 0: continue
    i = 0
    for target_id in paper["outCitations"]:
        i += 1
        graph.addEdge(
            paper["title"] + "__" + str(i), # edge label
            id, target_id) # source label, target label

################################################################
print("[#] Writing file:")

graph.write("../net/")

# print(graph.getAllIndegrees())