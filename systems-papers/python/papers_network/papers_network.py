import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from utils.json import *

DIR_PARENT = "papers_network/"
DIR_DATA   = DIR_PARENT + "data/"
DIR_GEPHI  = DIR_PARENT + "gephi/"
DIR_FIGS   = DIR_PARENT + "figs/"

class PapersNetwork:
  def __init__(self):
    self.papers_data = None # paper_id  => paper
    self.papers      = {}   # paper_id  => [author_id]
    self.authors     = {}   # author_id => [paper_id]
    
    self.graph = nx.Graph()
    self.attributes = {}

  def write(self):
    suffix = "".join([ "_" + k + "=" + v for (k,v) in self.attributes.items() ])
    nx.write_gexf(self.graph, DIR_GEPHI+"papers-network"+suffix+".gexf")

  def add_papers(self, papers):
    self.papers_data = papers
    for paper_id, paper in papers.items(): self.add_paper(paper)

  def add_paper(self, paper):
    paper_id = paper["id"]

    author_ids = []
    # to add each author
    def add_author(author_id):
      # add to papers
      author_ids.append(author_id)
      # add to authors
      if not author_id in self.authors: self.authors[author_id] = []
      self.authors[author_id].append(paper_id)

    # collect paper's authors
    for author in paper["authors"]:
      author_id = extract_author_id(author)
      add_author(author_id)
    self.papers[paper_id] = author_ids

  def fill_graph(self):
    venues = (
      # target conferences
      "asplos atc ccgrid ccs cidr cloud cluster conext euro-par eurosys fast hcw hipc hotcloud hoti hotos hotstorage hpca hpcc hpdc icac icdm icpe icpp igsc iiswc imc ipdps isc isca ispass kdd mascots micro middleware mobicom ndss nsdi oopsla pact pldi podc pods ppopp sc sigcomm sigir sigmetrics sigmod sle socc sosp sp spaa systor vee " + \
      # extra conferences (not expected)
      "pacmpl iacr usenix pomacs"
    ).split()

    def get_venue_index(venue):
      for i in range(len(venues)):
        if venues[i] in venue: return i
      return -1

    # nodes: papers
    for paper_id, paper in self.papers_data.items():
      self.graph.add_node(paper_id)
      title = paper["title"] if "title" in paper else "no title"
      self.graph.node[paper_id]["title"] = title

      venue = paper["venue"].lower() \
        if ("venue" in paper) \
        else ("missing venue")
      venue_i = get_venue_index(venue)

      if venue_i == -1: print(venue)

      self.graph.node[paper_id]["venue-index"] = venue_i
      self.graph.node[paper_id]["venue"] = venue

    # edges: shared authors (collaborations)
    # for each paper p
    for paper_id, author_ids in self.papers.items():
      # for each author a of paper p
      for author_id in author_ids:
        # for each other paper p' by author a
        for p_id in self.authors[author_id]:
          if paper_id != p_id:
            self.graph.add_edge(paper_id, p_id)

  def print_statistics(self):
    print("-------------------------------------------")
    print("-- Graph Statistics -----------------------")
    print()
    print("   isolates:", nx.number_of_isolates(self.graph))
    print("    density:", nx.density(self.graph))
    print("    bridges:", len(list(nx.bridges(self.graph))))
    print("    cliques:", nx.graph_clique_number(self.graph))
    print(" conn-comps:", nx.number_connected_components(self.graph))
    print()
    print("-------------------------------------------")

  def calculate_centralities(self):
    # dump calculated data
    dump_json(nx.degree_centrality(self.graph),
      DIR_DATA + "degree_centralities")
    dump_json(nx.eigenvector_centrality(self.graph),
      DIR_DATA + "eigenvector_centralities")
    dump_json(nx.closeness_centrality(self.graph),
      DIR_DATA + "closeness_centralities")
    dump_json(nx.betweenness_centrality(self.graph),
      DIR_DATA + "betweenness_centralities")

  def fill_node_centralities(self, centrality_name):
    data = load_json(DIR_DATA+centrality_name+"_centralities")
    # set color attributes
    for node, value in data.items():
      self.graph.node[node][centrality_name+"-centrality"] = value
    # set graph attribute
    self.attributes["centrality"] = centrality_name

  # remove all nodes except for those in the cc_ranked connected component,
  # where components are ranked from largest to smallest node count
  def isolate_component(self, cc_rank):
    self.graph = \
      sorted(nx.connected_component_subgraphs(self.graph),
        key = len, reverse = True) \
      [cc_rank]

    self.attributes["cc-rank"] = cc_rank

      


def extract_author_id(author):
  # success - author in data set (has id)
  if "ids" in author and len(author["ids"]) > 0: return author["ids"][0]
  # failure - author not in data set (doesn't have id)
  else: return False
