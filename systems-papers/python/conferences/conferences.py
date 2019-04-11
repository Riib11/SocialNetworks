import utils.data as data
import semantic_scholar.s2data as s2data
import csv
from utils.json import *

VERSION = "1.0"

DIR_PARENT = "conferences/"
DIR_DATA   = DIR_PARENT+"data/"

FP_S2_CONFERENCES = DIR_DATA+"s2_conferences"+"_v="+VERSION+".json"
FP_S2_KEYS = DIR_DATA+"s2_keys.json"
FP_S2_KEYS_CSV = DIR_DATA+"s2_keys.csv"
FP_KEYS_S2_CSV = DIR_DATA+"keys_s2.csv"

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

################################################################################
################################################################################

def get_s2_keys():
  # all_conf_papers : [(conf_name, conf_papers)]
  all_conf_papers = list(get_each_conference_papers())
  papers = s2data.get_dict_gA()

  def match_paper_title_with_key(paper_title):
    for conf_name, conf_papers in all_conf_papers:
      for paper in conf_papers:
        if paper_title.lower() == paper["title"].lower():
          return paper["key"]

  # s2_paper_keys :: paper_id => key
  s2_paper_keys = {}
  
  # build s2_paper_keys by iterating through all s2 papers
  for paper_id, paper in papers.items():
    key = match_paper_title_with_key(paper["title"])
    if key:
      s2_paper_keys[paper_id] = key
      # print("[*]", paper["title"])
    else:
      # print("[!!!]", paper["title"])
      pass
  
  return s2_paper_keys

def dump_s2_keys():
  s2_keys = get_s2_keys()
  dump_json(s2_keys, FP_S2_KEYS)

def load_s2_keys():
  return load_json(FP_S2_KEYS)

def dump_s2_keys_csv():
  s2_keys = load_s2_keys()
  with open(FP_S2_KEYS_CSV, "w+") as file:
    w = csv.writer(file)
    w.writerow(["paper_id", "paper_key"])
    for id, key in s2_keys.items():
      w.writerow([id, key])

def dump_keys_s2_csv():
  s2_keys = load_s2_keys()
  with open(FP_KEYS_S2_CSV, "w+") as file:
    w = csv.writer(file)
    w.writerow(["paper_key", "paper_id"])
    for id, key in s2_keys.items():
      w.writerow([key, id])

################################################################################
################################################################################

if __name__ == "__main__":
  # dump_s2_conferences()
  # dump_s2_keys()
  dump_s2_keys_csv()
  dump_keys_s2_csv()
