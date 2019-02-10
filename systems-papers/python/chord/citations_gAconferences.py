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
import matplotlib.pyplot as plt
import numpy as np

# modules
from gexf.gexf import GEXF
import utils.data as u_data
import semantic_scholar.s2data as s2data
import chord.chord as chord
import chord.chord_colors as chord_colors

################################################################
# parameters

threshold = 150

################################################################
print("[#] Loading Data:")

gA = s2data.get_dict_gA()
gB = s2data.get_dict_gB()

################################################################
print("[#] Analyzing Data:")

# { conference : { conference: #citations } }
conferences = {}

def inc_conf(source, target):
    if not source in conferences:
        conferences[source] = {}
    if not target in conferences[source]:
        conferences[source][target] = 0
    conferences[source][target] += 1

for id, paper in gA.items():
    conf = conf_utils.normalize_conference(
        paper["venue"])
    if len(conf) == 0: continue
    for target_id in paper["outCitations"]:
        try:
            target_paper = gB[target_id]
            target_conf = conf_utils.normalize_conference(
                target_paper["venue"])
            if len(target_conf) == 0: continue
            inc_conf(conf, target_conf)
        except: pass

################################################################
print("[#] Writing file:")

conferences_list = list(conferences.keys())
l = len(conferences_list)
def to_conf_ind(conf): return conferences_list.index(conf)

passes = [0,0]

# X[i,j] corresponds to flux from i to j
X = [ [ 0 for _ in range(l) ] for _ in range(l) ]
for i in range(len(conferences_list)):
    source = conferences_list[i]
    for target, flux in conferences[source].items():
        passes[ 0 if flux < threshold else 1 ] += 1
        if flux < threshold: continue
        if not target in conferences_list: continue
        j = to_conf_ind(target)
        X[i][j] = flux

print(passes)

plt.figure(figsize=(6,6))
chord.chordDiagram( np.array(X), plt.axes([0,0,1,1]), chord_colors.colors )
plt.show()