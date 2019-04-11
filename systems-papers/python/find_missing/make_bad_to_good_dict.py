import utils.strings as util_str
import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
import json
from tqdm import tqdm

known        = s2_data.get_dict_gA()
id_to_paper  = { (p["id"] if "id" in p else p["paperId"])  }
known_titles = [ p["title"] for p in known.values() ]
title_to_id  = { p["title"] : p_id for p_id, p in known.items() }

PARENT_DIR         = "find_missing/"
BAD_TITLE_TO_ID_FN = PARENT_DIR + "bad_title_to_id.json"
PARTIAL_TO_GOOD_FN = PARENT_DIR + "partial_to_good.json"
BAD_TO_GOOD_FN     = PARENT_DIR + "bad_to_good.json"

def load_json(fn):
  with open(fn, "r+") as f: return json.load(f)

def save_json(fn, obj):
  with open(fn, "w+") as f: json.dump(obj, f, indent=4)

bad_title_to_id = load_json(BAD_TITLE_TO_ID_FN)
partial_to_good = load_json(PARTIAL_TO_GOOD_FN)

# get good titles for bad titles
bad_title_to_good_title = \
  { bad_title : id_to_paper[p_id]["title"]
    for bad_title, p_id in bad_title_to_id.items() }

# merge with partial => good
for partial_title, good_title in partial_to_good.items():
  bad_title_to_good_title[partial_title] = good_title

save_json(BAD_TO_GOOD_FN, bad_title_to_good_title)
print("length:", len(bad_title_to_good_title))
