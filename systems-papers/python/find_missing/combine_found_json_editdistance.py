from utils.json import *
import glob

PARENT_DIR = "find_missing/"
DATA_DIR = PARENT_DIR + "data/"
FOUND_JSON_EDITDISTANCE_DIR = DATA_DIR + "json_editdistance/"
FOUND_EDITDISTANCE_ALL_FN = DATA_DIR + "found_all_editdistance.json"

d = {}
for fn in glob.glob(FOUND_JSON_EDITDISTANCE_DIR+"*"):
  found_paper = load_json(fn)
  p_id = found_paper["paperId"]
  found_paper["id"] = p_id
  d[p_id] = found_paper

dump_json(d, FOUND_EDITDISTANCE_ALL_FN)
print(len(d))
