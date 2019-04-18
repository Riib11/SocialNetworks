import utils.strings as util_str
import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
import utils.json as u_json
from tqdm import tqdm

DATA_DIR = "find_missing/data/"
MISSING_RAWTITLES_FN    = DATA_DIR + "missing_rawtitles.txt"
MISSING_RAWTITLES_ED_FN = DATA_DIR + "missing_rawtitles_editdistance.txt"
RAWTITLE_TO_S2TITLE_FN  = DATA_DIR + "rawtitle_to_s2title.json"
RAWTITLE_TO_S2ID_FN     = DATA_DIR + "rawtitle_to_s2id.json"

MISSING_RAWTITLES_ED_IDS_FN = DATA_DIR + "missing_rawtitles_editdistance_ids.txt"

s2id_to_s2paper = s2_data.get_dict_gA()

with open(MISSING_RAWTITLES_ED_FN, "r+") as file: found_rawtitles = [ line.strip() for line in file ]
with open(MISSING_RAWTITLES_ED_IDS_FN, "r+") as file: found_s2ids = [ line.strip() for line in file ]

rawtitle_to_s2id = u_json.load_json(RAWTITLE_TO_S2ID_FN)
rawtitle_to_s2title = u_json.load_json(RAWTITLE_TO_S2TITLE_FN)

for i in range(len(found_rawtitles)):
  found_rawtitle = found_rawtitles[i]
  found_s2id     = found_s2ids[i]
  if found_s2id == "!": continue
  if not found_s2id in s2id_to_s2paper:
    print("unfound:",found_s2id)
    continue
  rawtitle_to_s2id[found_rawtitle] = found_s2id
  rawtitle_to_s2title[found_rawtitle] = s2id_to_s2paper[found_s2id]["title"]

u_json.dump_json(rawtitle_to_s2id, RAWTITLE_TO_S2ID_FN)
u_json.dump_json(rawtitle_to_s2title, RAWTITLE_TO_S2TITLE_FN)
