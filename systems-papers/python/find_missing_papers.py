import utils.strings as util_str
import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
from tqdm import tqdm

known        = s2_data.get_dict_gA()
known_titles = [ p["title"] for p in known.values() ]
title_to_id  = { p["title"] : p_id for p_id, p in known.items() }

confs = list(conf_data.get_each_conference_papers())

def is_known(paper_title):
  if paper_title in known_titles: return True
  for known_title in tqdm(known_titles):
    if util_str.editDistance(paper_title, known_title) <= 5:
      return True
  return False

missing_titles = []

for (conf_name, conf_papers) in confs:
  for paper in conf_papers:
    title = paper["title"]
    if not is_known(title):
      missing_titles.append(title)
      print(title)

print("total:", len(missing_titles))
