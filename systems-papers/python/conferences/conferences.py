import utils.data as data
import semantic_scholar.s2data as s2data
from utils.json import *

VERSION = "1.0"

DIR_PARENT = "conferences/"
DIR_DATA   = DIR_PARENT+"data/"

FP_S2_CONFERENCES = DIR_DATA+"s2_conferences"+"_v="+VERSION+".json"

def get_each_conference_papers():
  for conf_name, conf_dict in data.getAllConferences():
    yield conf_name, conf_dict["papers"]

# matches semantic scholar papers to their appropriate conference,
# as organized in /authors/data/conf/
def get_s2_conferences():
  # all_conf_papers : [(conf_name, conf_papers)]
  all_conf_papers = list(get_each_conference_papers())
  papers = s2data.get_dict_gA()

  def match_paper_title_with_conf(paper_title):
    for conf_name, conf_papers in all_conf_papers:
      for paper in conf_papers:
        # print(conf_name,":",paper["title"])
        if paper_title.lower() == paper["title"].lower():
          return conf_name

  s2_paper_confs = {} # paper_id => conf_name
  # iterate through all s2 papers
  # papers = { k:v for k,v in list(papers.items())[1:10] }
  for paper_id, paper in papers.items():
    conf_name = match_paper_title_with_conf(paper["title"])
    if conf_name:
      s2_paper_confs[paper_id] = conf_name
      # print("[*]", paper["title"])
    else:
      pass
      # print("[!!!]", paper["title"])
  
  return s2_paper_confs

def dump_s2_conferences():
  s2_paper_confs = get_s2_conferences()
  dump_json(s2_paper_confs, FP_S2_CONFERENCES)

def load_s2_conferences():
  return load_json(FP_S2_CONFERENCES)

if __name__ == "__main__":
  dump_s2_conferences()

