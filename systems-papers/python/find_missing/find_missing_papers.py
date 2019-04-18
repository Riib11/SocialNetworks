import utils.strings as util_str
import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
import utils.json as u_json
from tqdm import tqdm

DATA_DIR = "find_missing/data/"
MISSING_RAWTITLES_FN   = DATA_DIR + "missing_rawtitles.txt"
RAWTITLE_TO_S2TITLE_FN = DATA_DIR + "rawtitle_to_s2title.json"
RAWTITLE_TO_S2ID_FN    = DATA_DIR + "rawtitle_to_s2id.json"

conferences = list(conf_data.get_each_conference_papers())
rawpapers = sum([ conf_papers for conf_name, conf_papers in conferences ], [])

known_papers = s2_data.get_dict_gA().values()

match_threshold = 5
def is_match(s1, s2):
  return s1.lower() == s2.lower()

rawtitle_to_s2title = {}
rawtitle_to_s2id    = {}

def is_known(rawpaper):
  rawtitle = rawpaper["title"]
  for paper in known_papers:
    known_title = paper["title"]
    if is_match(rawtitle, known_title):
      rawtitle_to_s2title[rawtitle] = known_title
      rawtitle_to_s2id[rawtitle] = paper["id"] if "id" in paper else paper["paperId"]
      return True
  return False

missing_rawpapers = [ rawpaper for rawpaper in tqdm(rawpapers) if not is_known(rawpaper) ]

print(len(missing_rawpapers), " = missing raw papers:")
print(len(rawtitle_to_s2id),   "= entries for (raw title => s2 title)")

with open(MISSING_RAWTITLES_FN, "w+") as file:
  [ file.write(rawpaper["title"] + "\n") for rawpaper in missing_rawpapers ]

u_json.dump_json(rawtitle_to_s2title, RAWTITLE_TO_S2TITLE_FN)
u_json.dump_json(rawtitle_to_s2id, RAWTITLE_TO_S2ID_FN)
