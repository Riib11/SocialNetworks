"""

Creates a network of paper citations.

Info:

Nodes:
- represent an individual paper, which may or may not be in the data set.
- are identified by their id in the semantic-scholar database

Edges:
- are directed and represent the source paper's citation of the target paper.
- are identified by the key of the source paper with a unique suffix (since there are multiple citations per source)

"""

# utilities
import sys
import os
import numpy as np
import utils.shared_utils as utils
import utils.colors as u_colors
import utils.combinatorics as u_combos
from utils.strings import clean
from tqdm import tqdm

# modules
from gexf.gexf import GEXF
from net.net import NET
import utils.data as u_data
import papers.paper_features as p_features

#----------------------------------------------------------------------------------
# To get running:
# - replace 'data dir path' with path to the semantic scholar database
# - make sure that you can accurately search for papers. use `ss3querytest.py`
# - tune thresholds (use random sampling to justify)
#----------------------------------------------------------------------------------

def generate():

    # search init
    s3 = sssearch.SSSearch(
        # data dir path
        u_data.semantic_scholar_dir,
        { # thresholds
            "author": 50,
            "title": 50,
            "year": 2
        })
    
    # graph init
    graph = NET("network_citation_net")

    # TODO: color attribute for each paper
    # TODO: print statisics:

    # iterate through papers
    conf_filenames = [ fn for fn in u_data.getConferenceFilenames() ]
    conf_filenames = conf_filenames[:10]

    print("------------------------------------------------")
    print("[#] Analyzing Data:")
    for conf_filename in tqdm(conf_filenames):
        conf_name = conf_filename.replace(".json","")
        data = u_data.getPapers(conf_filename)
        papers = data['papers']
        for paper in papers:
            bibtex = p_features.getCitationsData(key)
            s3entry, _ = s3.query("2017",None,paper["title"])
            # Dict organization
            # paper   : {key, title, authors}
            # bibtex  : {author, journal, title, year}
            # s3entry : {id, authors, title, abstract, journalName}
            
            # make node for this paper
            graph.addNode(s3entry["id"], {}) # TODO: node attributes
            
            # make edges to papers that this paper cites
            e_id = key
            uid_suffix = 0
            for i in range(bibtex["size"]):
                s3cit, _ = s3.query(
                    bibtex["year"],
                    bibtex["author"],
                    bibtex["title"])
                graph.addNode(s3cit["id"], {}) # TODO: node attributes
                graph.addEdge(e_id+str(uid_suffix), s3entry["id"], s3cit["id"])
                uid_suffix += 1

    print("------------------------------------------------")
    print("[%] Writing file:")
    graph.write(u_data.systems_papers_directory + "net/")
