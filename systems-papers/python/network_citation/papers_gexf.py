"""

Creates a network of paper citations.

- Info:

    - Nodes represent an individual paper, which may or may not be in the data set.

    - Edges are directed and represent the source paper's citation of the target paper.

"""

# utilities
import sys
import os
import numpy as np
import utils.shared_utils as utils
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
    graph = GEXF("citations_papers")
    # parameters
    graph.setParameter("graph", "defaultedgetype", "directed")
    # attributes
    graph.addAttribute( "node", "conference" , "string", "" )
    graph.addAttribute( "node", "title"      , "string", "" )
    graph.addAttribute( "node", "year"      , "string", "" )


    # TODO: color attribute for each paper
    # TODO: print statisics:

    ################################################################
    print("[#] Loading Data:")
    
    gA = s2data.get_dict_gA()

    ################################################################
    print("[#] Analyzing Data:")

    def safeindex(d,k):
        return d[k] if k in d else "MISSING"
    
    for id, paper in gA.items():
        graph.addNode(
            id, {
            "title"      : safeindex(paper,"title"),
            "conference" : safeindex(paper,"venue"),
            "year"       : str(safeindex(paper,"year"))
        })
        for out_id in paper["outCitations"]:
            graph.addEdge(safeindex(paper,"title"), id, out_id, 1)

    ################################################################
    print("[#] Writing file:")

    graph.write("/home/blancheh/SystemsAnalysis/systems-papers/gexf/")

generate()
