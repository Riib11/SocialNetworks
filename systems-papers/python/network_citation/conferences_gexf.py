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
from gexf.gexf import GEXF
import utils.data as u_data
import semantic_scholar.s2data as s2data

def generate():

    ################################################################
    print("[#] Initializing GEXF")
    
    # graph init
    graph = GEXF("citations_conferences")
    # parameters
    graph.setParameter("graph", "defaultedgetype", "directed")
    # attributes
    # graph.addAttribute( "node", "conference" , "string", "" )
    # graph.addAttribute( "node", "title"      , "string", "" )
    # graph.addAttribute( "node", "year"      , "string", "" )


    # TODO: color attribute for each paper
    # TODO: print statisics:

    ################################################################
    print("[#] Loading Data:")
    
    gA = s2data.get_dict_gA()
    gB = s2data.get_dict_gB()

    ################################################################
    print("[#] Analyzing Data:")

    conferences = []
    edge_id = 0
    missing_count = 0

    def addNode_safe(conf):
        if not conf in conferences:
            graph.addNode(conf, {})
            conferences.append(conf)

    for source_id, source_paper in gA.items():
        
        # source node
        source_conf = conf_utils.normalize_conference(
            source_paper["venue"])
        if len(source_conf) == 0: continue
        addNode_safe(source_conf)

        # for each outcite
        for target_id in source_paper["outCitations"]:
            
            if not target_id in gB:
                missing_count += 1
                continue

            # target node
            target_conf = conf_utils.normalize_conference(
                gB[target_id]["venue"])
            if len(target_conf) == 0: continue
            addNode_safe(target_conf) 
            
            # edge
            graph.addEdge(str(edge_id), source_conf, target_conf)
            edge_id += 1

    print("[>] missing count:",missing_count)

    ################################################################
    print("[#] Writing file:")

    graph.write("/home/blancheh/SystemsAnalysis/systems-papers/gexf/")

generate()
