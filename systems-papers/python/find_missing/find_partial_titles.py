import utils.strings as util_str
import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
import json
from tqdm import tqdm

PARENT_DIR         = "find_missing/"
PARTIAL_FN         = PARENT_DIR + "partial_titles.txt"
PARTIAL_TO_GOOD_FN = PARENT_DIR + "partial_to_good.json"

known        = s2_data.get_dict_gA()
known_titles = [ p["title"] for p in known.values() ]
title_to_id  = { p["title"] : p_id for p_id, p in known.items() }

with open(PARTIAL_FN) as file:
  partial_titles = [ line.strip() for line in file ]

match_threshold = 5
def is_match(s1, s2):
  return util_str.editDistance(s1, s2) <= match_threshold

def match_to_good_title(partial_title):
  for known_title in tqdm(known_titles):
    if partial_title.lower() == known_title.lower(): return known_title
    # if is_match(partial_title, known_title):
    #   return known_title
  return None

# partial_to_good :: partial_title => good_title
partial_to_good = {}

unfound_count = 0

for partial_title in tqdm(partial_titles):
  good_title = match_to_good_title(partial_title)
  if good_title:
    partial_to_good[partial_title] = good_title
  else:
    # print("unfound:", partial_title)
    unfound_count += 1

found_count = len(partial_to_good)

with open(PARTIAL_TO_GOOD_FN, "w+") as file:
  json.dump(partial_to_good, file, indent=4)

found_percent = 100 * found_count / (found_count + unfound_count)

print("unfound count:", unfound_count)
print("  found count:", found_count,"({0}%)".format(found_percent))

