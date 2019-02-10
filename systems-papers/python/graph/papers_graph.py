import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from utils.json import *

class AuthorsGraph:
  def __init__(self):
    self.authors = {} # author_id => paper_id
    self.papers  = {} # paper_id  => paper (dict)
    self.graph = nx.Graph()

  # def draw(self): nx.draw(self.graph)
  def write(self): nx.write_gexf(self.graph, "graph/papers-graph.gexf")

  def add_paper(self, paper):
    paper_id = paper["id"]
    self.papers[paper_id] = paper
    for author in paper["authors"]:
      author_id = extract_author_id(author)
      if author_id:
        self.add_author_id(author_id)
        self.add_author_paper(author_id, paper_id)
    return paper_id

  def get_paper(self, paper_id): return self.papers[paper_id]

  def add_author_id(self, author_id):
    if not author_id in self.authors:
      self.authors[author_id] = []

  # add to author a paper they wrote
  def add_author_paper(self, author_id, paper_id):
    self.get_author_papers(author_id).append(paper_id)

  def get_author_papers(self, author_id): return self.authors[author_id]

  # get author list (in data set) of the given paper
  def get_paper_authors(self, paper_id):
    for author in self.get_paper(paper_id)["authors"]:
      author_id = extract_author_id(author)
      if author_id: yield author_id

  # gets list of authors that the given author has collaborated with
  def get_author_collaborators(self, author_id):
    for paper_id in self.get_author_papers(author_id):
      for a_id in self.get_paper_authors(paper_id):
        if a_id != author_id: yield a_id

  # fill self.graph : nx.Graph
  def fill_graph(self):
    # nodes
    for author_id in self.authors.keys():
      self.graph.add_node(author_id)
    # edges
    for author_id, paper_ids in self.authors.items():
      for a_id in self.get_author_collaborators(author_id):
        self.graph.add_edge(author_id, a_id)

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
      "graph/data/degree_centralities")
    dump_json(nx.eigenvector_centrality(self.graph),
      "graph/data/eigenvector_centralities")
    dump_json(nx.closeness_centrality(self.graph),
      "graph/data/closeness_centralities")
    dump_json(nx.betweenness_centrality(self.graph),
      "graph/data/betweenness_centralities")

  def plot_centralities(self):
    plt.subplot(221)
    plt.title("Degree Centralities")
    plt.xlabel('Degree Centrality')
    plt.ylabel('Node Share')
    plt.grid(True)
    plt.hist(list(load_json("graph/data/degree_centralities").values()),
      70, histtype="bar", facecolor="blue", alpha=1.0)

    plt.subplot(222)
    plt.title("Eigenvector Centralities")
    plt.xlabel('Eigenvector Centrality')
    plt.ylabel('Node Share')
    plt.grid(True)
    plt.hist(list(load_json("graph/data/eigenvector_centralities").values()),
      20, histtype="bar", facecolor="blue", alpha=1.0)

    plt.subplot(223)
    plt.title("Closeness Centralities")
    plt.xlabel('Closeness Centrality')
    plt.ylabel('Node Share')
    plt.grid(True)
    plt.hist(list(load_json("graph/data/closeness_centralities").values()),
      70, histtype="bar", facecolor="blue", alpha=1.0)

    plt.subplot(224)
    plt.title("Betweenness Centralities")
    plt.xlabel('Betweenness Centrality')
    plt.ylabel('Node Share')
    plt.grid(True)
    plt.hist(list(load_json("graph/data/betweenness_centralities").values()),
      40, histtype="bar", facecolor="blue", alpha=1.0)
    
    plt.tight_layout()
    plt.show()

  def to_adjacency_matrix(self):
    # matrix of author-author collaborations
    matrix = [[ 0
      for _ in range(len(self.authors)) ]
      for _ in range(len(self.authors))  ]
    # calculate author indices
    authors_is = {}
    author_i = 0
    for author_id in self.authors.keys():
      authors_is[author_id] = author_i
      author_i += 1
    # fill author-author edges
    for author_id in self.authors.keys():
      for a_id in self.get_author_collaborators(author_id):
        matrix[ authors_is[author_id] ][ authors_is[a_id] ] = 1
    return np.matrix(matrix)

  # transpose of adjacency matrix
  def to_transformed_adjacency_matrix(self):
    return self.to_adjacency_matrix().T

def extract_author_id(author):
  # success - author in data set (has id)
  if "ids" in author and len(author["ids"]) > 0: return author["ids"][0]
  # failure - author not in data set (doesn't have id)
  else: return False
