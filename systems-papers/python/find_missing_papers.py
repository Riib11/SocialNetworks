import utils.strings as util_str
import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
from tqdm import tqdm

known        = s2_data.get_dict_gA()
known_titles = [ p["title"] for p in known.values() ]
title_to_id  = { p["title"] : p_id for p_id, p in known.items() }

conferences = list(conf_data.get_each_conference_papers())
papers      = sum([ conf_papers for conf_name, conf_papers in conferences ], [])

match_threshold = 5
def is_match(s1, s2): return util_str.editDistance(s1, s2) <= match_threshold

def is_known(paper_title):
  if paper_title in known_titles: return True
  return any ([ is_match(paper_title, known_title) for known_title in known_titles ])

missing_titles = []

for paper in tqdm(papers):
  title = paper["title"]
  if not is_known(title): missing_titles.append(title)

print("\n".join(missing_titles))
print("="*50)
print("total:", len(missing_titles))

result_fn = "find_missing_papers_result.txt"
print("missing paper titles written to:", result_fn)
with open(result_fn, "w+") as file: file.write("\n".join(missing_titles))
