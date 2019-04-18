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

with open(MISSING_RAWTITLES_FN, "r+") as file: rawtitles = [ line.strip() for line in file ]

known_papers = s2_data.get_dict_gA().values()

match_threshold = 5
is_match = lambda s1, s2: util_str.editDistance(s1.lower(), s2.lower()) <= match_threshold

# append new matches to old dicts
rawtitle_to_s2title = u_json.load_json(RAWTITLE_TO_S2TITLE_FN)
rawtitle_to_s2id    = u_json.load_json(RAWTITLE_TO_S2ID_FN)

def is_known(rawtitle):
  for paper in known_papers:
    known_title = paper["title"]
    if is_match(rawtitle, known_title):
      rawtitle_to_s2title[rawtitle] = known_title
      rawtitle_to_s2id[rawtitle] = paper["id"] if "id" in paper else paper["paperId"]
      return True
  return False

# rawtitles = rawtitles[:5] # for testing
missing_rawtitles = [ rawtitle for rawtitle in tqdm(rawtitles) if not is_known(rawtitle) ]

print(len(missing_rawtitles), " = missing raw titles:")
print(len(rawtitle_to_s2id),   "= entries for (raw title => s2 title)")

# write the rawtitles that are STILL missing
# after comparing edit distances
with open(MISSING_RAWTITLES_ED_FN, "w+") as file:
  [ file.write(rawtitle + "\n") for rawtitle in missing_rawtitles ]

u_json.dump_json(rawtitle_to_s2title, RAWTITLE_TO_S2TITLE_FN)
u_json.dump_json(rawtitle_to_s2id, RAWTITLE_TO_S2ID_FN)
