import semantic_scholar.s2data as s2_data
import conferences.conferences as confs_data

class ConferenceCollaborationsNetwork:

  def __init__(self):
    self.paper_conferences = conf_data.load_s2_conferences()
    self.papers = s2data.get_dict_gA()

    self.attributes = {} # keep track of modifications to graph

    self.graph = nx.Graph()

  def write(self):
    suffix = "".join(
      [ "_" + k + "=" + str(v)
      for (k,v) in self.attributes.items() ])
    nx.write_gexf(self.graph,
      DIR_GEPHI + "conference-collaborations-network"+suffix+".gexf")

  def fill():
    #
    # create author collaborations
    #
    collabs = {} # author_id => [( conf_name, paper_id, [author_id] )]

    def add_collab(author_id, conf_name, paper_id, collab_ids):
      if not author_id in collabs: collabs[author_id] = []
      collabs[author_id].append((conf_name, paper_id, collab_ids))

    for paper in self.papers:
      paper_id = paper["id"]
      conf_name = self.paper_conferences[paper_id]
      author_ids = \
        [ extract_author_id(author_id)
          for author_id in paper["authors"]
          if extract_author_id(author_id) ]
      
      for i in range(len(author_ids)):
        author_id = author_ids[i]
        collab_ids = author_ids[:i] + author_ids[i+1:]
        add_collab(author_id, conf_name, paper_id, collab_ids)

    # 
    # create conference collaborations
    # 
    conf_collabs = {} # conf_name => (conf_name => set<str>)

    def add_conf_collab(src_conf_name, tgt_conf_name, paper_id):
      if not src_conf_name in conf_collabs: conf_collabs[src_conf_name] = {}
      if not tgt_conf_name in conf_collabs[src_conf_name]: conf_collabs[src_conf_name] = set()
      conf_collabs[src_conf_name].add(paper_id)

    for author_id, (src_conf_name, paper_id, collab_ids) in collabs.items():
      for collab_id in collab_ids:
        for (tgt_conf_name, paper_id, author_id) in collabs[collab_id]:
          add_conf_collab(src_conf_name, tgt_conf_name, paper_id)

    #
    # add nodes
    #
    for tgt_conf_name in conf_collabs.keys(): self.graph.add_node(conf_name)

    #
    # add edges
    #
    for src_conf_name, tgt_conf_dict in conf_collabs.items():
      for tgt_conf_name, paper_ids in tgt_conf_dict.items():
        self.add_edge(src_conf_name, tgt_conf_name, weight=len(paper_ids))


def extract_author_id_name(author):
  # success - author in data set (has id)
  if "ids" in author and "name" in author and len(author["ids"]) > 0:
    return author["ids"][0], utils.normalized_author_name(author["name"])
  # failure - author not in data set (doesn't have id)
  else:
    # debug(author)
    return (False, False)

def extract_author_id(author):
  if "ids" in author and len(author["ids"]) > 0: return author["ids"][0]
  else: return False

if __name__ == "__main__":
  papers = s2_data.get_dict_gA()
  # print(list(papers.items())[0])

  confs = confs_data.get_each_conference_papers()
  for a,b in confs:
    print(a,b)
    quit()
