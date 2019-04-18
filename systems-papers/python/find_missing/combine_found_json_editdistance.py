from utils.json import *
import glob

PARENT_DIR = "find_missing/"
DATA_DIR = PARENT_DIR + "data/"

FOUND_JSON_EDITDISTANCE_DIR = DATA_DIR + "json_editdistance/"
FOUND_EDITDISTANCE_ALL_FN   = DATA_DIR + "found_all_editdistance.json"
MISSING_RAWTITLES_ED_IDS_FN = DATA_DIR + "missing_rawtitles_editdistance_ids.txt"
MISSING_RAWTITLES_ED_FN     = DATA_DIR + "missing_rawtitles_editdistance.txt"

RAWTITLE_TO_S2ID_FN         = DATA_DIR + "rawtitle_to_s2id.json"
RAWTITLE_TO_S2TITLE_FN      = DATA_DIR + "rawtitle_to_s2title.json"

with open(MISSING_RAWTITLES_ED_IDS_FN, "r+") as file: missing_rawtitles_ed_ids = [ l.strip() for l in file ]
with open(MISSING_RAWTITLES_ED_FN,     "r+") as file: missing_rawtitles_ed     = [ l.strip() for l in file ]

s2id_to_rawtitle = lambda s2id: missing_rawtitles_ed[missing_rawtitles_ed_ids.index(s2id)]

rawtitle_to_s2id = load_json(RAWTITLE_TO_S2ID_FN)
rawtitle_to_s2title = load_json(RAWTITLE_TO_S2TITLE_FN)

found_s2id_to_paper = {}
for fn in glob.glob(FOUND_JSON_EDITDISTANCE_DIR+"*"):
  found_paper = load_json(fn)
  found_s2id = found_paper["paperId"]
  found_title = found_paper["title"]
  found_rawtitle = s2id_to_rawtitle(found_s2id)
  
  found_paper["id"] = found_s2id
  found_s2id_to_paper[found_s2id] = found_paper
  
  rawtitle_to_s2title[found_rawtitle] = found_title
  rawtitle_to_s2id[found_rawtitle] = found_s2id

dump_json(found_s2id_to_paper, FOUND_EDITDISTANCE_ALL_FN)
print("len(found_s2id_to_paper) =",len(found_s2id_to_paper))

# update (rawtitle => *) dicts
dump_json(rawtitle_to_s2id, RAWTITLE_TO_S2ID_FN)
dump_json(rawtitle_to_s2title, RAWTITLE_TO_S2TITLE_FN)
print("len(rawtitle_to_s2id) =", len(rawtitle_to_s2id))

