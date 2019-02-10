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
        - Node: Colored by the `color_attribute` of the author that the node reprents. Is that max of all values found among data/authors/*.json. If the target attribtute is not avaliable for a node, the node is colored black.
        - Edge: Colored by the maximum value of the nodes connected by this edge.

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
from net.net import NET
import utils.data as u_data
import authors.author_features as a_features

directory = u_data.systems_papers_directory+"net/"

def generate(color_attribute):

    # graph
    graph = NET("collaboration_net"+"_color="+color_attribute)

    # color attribute for each author
    color_attribute_dict = a_features.getAllAuthorsAttribute(color_attribute)
    color_attribute_dict_values = [ hind for hind in color_attribute_dict.values() ]
    color_attribute_min = min(color_attribute_dict_values)
    color_attribute_max = max(color_attribute_dict_values)
    with open(directory+graph.name+"_attributes.txt", "w+") as file:
        file.write("name hindex\n")
        for a_name, hind in color_attribute_dict.items():
            file.write("\""+a_name+"\""+" "+str(hind)+"\n")
    # print statisics:
    print("------------------------------------------------")
    print(color_attribute + " statistics:")
    print(" - min    :", color_attribute_min)
    print(" - max    :", color_attribute_max)
    print(" - mean   :", np.mean(color_attribute_dict_values))
    print(" - median :", np.median(color_attribute_dict_values))
    print(" - std    :", np.std(color_attribute_dict_values))

    def colorAttributeToColor(val):
        norm = (val - color_attribute_min) / color_attribute_max
        return u_colors.RGBToHexColor(norm, 0.0, 1-norm)

    # iterate through papers
    conf_filenames = [ fn for fn in u_data.getConferenceFilenames() ]

    print("------------------------------------------------")
    features = a_features.getAllAuthorFeatures()
    print("[#] Analyzing Data:")
    for conf_filename in tqdm(conf_filenames):
        data = u_data.getPapers(conf_filename)
        papers = data['papers']
        for paper in papers:
            # paper data
            uid_suffix   = 0 # make same-paper edges unique
            paper_key    = paper['key']
            author_names  = [ utils.author_name(a)[0]
                              for a in paper['authors'] ]
            author_unames = [ a_features.getAuthorUName(a,features)
                              for a in paper['authors']]
            
            # iterate through collaborations
            indecies = [ i for i in range(len((author_names)))]
            for (i1,i2) in u_combos.pairs_unordered(indecies):
                vals = [0] # for calculating max val in pair
                aus = [ author_unames[i1] , author_unames[i2] ]
                ans = [ author_names[i1]  , author_names[i2] ]
                for i in range(2):
                    au, an = aus[i], ans[i]
                    # attributes
                    a_attrs = {}
                    # color_attribute
                    if an in color_attribute_dict:
                        val = color_attribute_dict[an]
                        vals.append(val)
                        a_attrs[color_attribute] = val
                        # a_attrs["color"] = colorAttributeToColor(val)
                    # add node to graph
                    graph.addNode(au, a_attrs)
                # add edge to graph
                e_attrs = { "color": colorAttributeToColor(max(vals)) }
                weight  = 1
                graph.addEdge(paper_key+"_"+str(uid_suffix),
                    aus[0], aus[1], weight, e_attrs)
                uid_suffix += 1

    print("------------------------------------------------")
    print("[%] Writing file:")
    graph.write(directory)
