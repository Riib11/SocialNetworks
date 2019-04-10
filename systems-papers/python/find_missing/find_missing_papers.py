import utils.strings as util_str
import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
from tqdm import tqdm

VERSION = 2

source_fn = "finding_missing/find_missing_papers_result.txt"
target_fn = "finding_missing/find_missing_papers_result_{0}.txt".format(VERSION)

known        = s2_data.get_dict_gA()
known_titles = [ p["title"] for p in known.values() ]
title_to_id  = { p["title"] : p_id for p_id, p in known.items() }

# DONE
# conferences  = list(conf_data.get_each_conference_papers())
# papers       = sum([ conf_papers for conf_name, conf_papers in conferences ], [])
# paper_titles = [ p["title"] for p in papers ]

with open(source_fn) as file:
  paper_titles = [ line.strip() for line in file ]

match_threshold = 5
def is_match(s1, s2):
  return s1.lower() == s2.lower()
  # return or util_str.editDistance(s1, s2) <= match_threshold

def is_known(paper_title):
  if paper_title in known_titles: return True
  return any([
      is_match(paper_title, known_title)
      for known_title in known_titles ])

missing_titles = \
  [ paper_title
    for paper_title in tqdm(paper_titles)
    if not is_known(paper_title) ]

print("="*80)
print("\n".join(missing_titles))
print("="*80)
print("total:", len(missing_titles))

print("missing paper titles written to:", target_fn)
with open(target_fn, "w+") as file: file.write("\n".join(missing_titles) + "\n")
