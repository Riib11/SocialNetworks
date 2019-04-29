import conferences.conferences as conf_data
import semantic_scholar.s2data as s2_data
import utils.json as u_json
import utils.strings as util_str
from tqdm import tqdm
from glob import glob

#############################################################################################################################
# paths
#############################################################################################################################

PARENT_DIR = "missing_keys/"

DATA_DIR                = PARENT_DIR + "data/"

MISSING_KEYS_FN         = DATA_DIR + "missing_keys.txt"
MISSING_TITLES_FN       = DATA_DIR + "missing_titles.txt"
MISSING_KEY_TO_TITLE_FN = DATA_DIR + "missing_key_to_title.json"

FOUND_S2URLS_FN              = DATA_DIR + "found_s2urls.txt"
FOUND_S2IDS_FN               = DATA_DIR + "found_s2ids.txt"
MISSING_KEY_TO_FOUND_S2ID_FN = DATA_DIR + "missing_key_to_found_s2id.json"

FOUND_S2_PAPERS_DIR        = DATA_DIR + "found_s2papers/"
DOWNLOAD_S2_PAPERS_FN      = PARENT_DIR + "wget_found_s2papers.sh"
COMBINED_FOUND_S2PAPERS_FN = DATA_DIR + "combined_found_s2papers.json"

#############################################################################################################################
# functions
#############################################################################################################################

def read_txt(fn):
    with open(fn, "r+") as file: return [ l.strip() for l in file if len(l.strip()) > 0 ]

def save_txt(arr, fn):
    with open(fn, "w+") as file: [ file.write(str(x)+"\n") for x in arr ]

get_missing_keys   = lambda: read_txt(MISSING_KEYS_FN)
get_missing_titles = lambda: read_txt(MISSING_TITLES_FN)

known_papers = sum(map(lambda x: x[1], conf_data.get_each_conference_papers()), [])

#############################################################################################################################

def calculate_missing_keys_to_titles():
    missing_keys = get_missing_keys()
    missing_titles_to_keys = {}
    for paper in tqdm(known_papers):
        for key in missing_keys:
            if key == paper["key"]:
                title = paper["title"]
                missing_titles_to_keys[key] = title
                missing_keys.remove(key)
                break
    return missing_titles_to_keys

def save_missing_keys_to_titles():
    missing_keys_to_titles = calculate_missing_keys_to_titles()
    u_json.dump_json(missing_keys_to_titles, MISSING_KEY_TO_TITLE_FN)

#############################################################################################################################

def calculate_missing_titles():
    missing_keys = get_missing_keys()
    missing_titles = []
    for paper in tqdm(known_papers):
        for key in missing_keys:
            if key == paper["key"]:
                missing_titles.append(paper["title"])
                missing_keys.remove(key)
                break
    return missing_titles

def save_missing_titles():
    missing_titles = calculate_missing_titles()
    save_txt(missing_titles, MISSING_TITLES_FN)

#############################################################################################################################

def calculate_found_s2ids():
    found_s2urls = read_txt(FOUND_S2URLS_FN)
    found_s2ids = []
    for s2url in found_s2urls:
        if s2url != "!":
            s2id = s2url[s2url.rindex("/")+1:]
            found_s2ids.append(s2id)
        else:
            found_s2ids.append("!")
    return found_s2ids

def save_found_s2ids():
    found_s2ids = calculate_found_s2ids()
    save_txt(found_s2ids, FOUND_S2IDS_FN)

#############################################################################################################################

def calculate_missing_key_to_found_s2id():
    missing_keys = read_txt(MISSING_KEYS_FN)
    found_s2ids  = read_txt(FOUND_S2IDS_FN)
    missing_key_to_found_s2id = {}
    for i in range(len(missing_keys)):
        key  = missing_keys[i]
        s2id = found_s2ids[i]
        missing_key_to_found_s2id[key] = s2id if s2id != "!" else None
    return missing_key_to_found_s2id

def save_missing_key_to_found_s2id():
    missing_key_to_found_s2id = calculate_missing_key_to_found_s2id()
    u_json.dump_json(missing_key_to_found_s2id, MISSING_KEY_TO_FOUND_S2ID_FN)

#############################################################################################################################

def make_download_found_s2papers():
    found_s2ids = read_txt(FOUND_S2IDS_FN)
    with open(DOWNLOAD_S2_PAPERS_FN, "w+") as file:
        file.write("# !/bin/bash\n")
        for s2id in found_s2ids:
            if s2id != "!":
                file.write(
                    "wget -O \"data/found_s2papers/{s2id}.json\" \"https://api.semanticscholar.org/v1/paper/{s2id}\"\n"\
                    .format(s2id=s2id))

def calculate_combined_found_s2papers():
    combined_found_s2papers = {}
    for fn in glob(FOUND_S2_PAPERS_DIR+"*.json"):
        paper = u_json.load_json(fn)
        s2id = paper["paperId"]
        paper["id"] = s2id
        combined_found_s2papers[s2id] = paper
    return combined_found_s2papers

def save_combined_found_s2papers():
    combined_found_s2papers = calculate_combined_found_s2papers()
    u_json.dump_json(combined_found_s2papers, COMBINED_FOUND_S2PAPERS_FN)

#############################################################################################################################
# main
#############################################################################################################################

if __name__ == "__main__":
    # step 1: get titles of papers to search for on s2
    # save_missing_titles()
    # save_missing_keys_to_titles()

    # step 2: record found s2ids and the mapping missing_key => found_s2id
    # save_found_s2ids()
    # save_missing_key_to_found_s2id()

    # step 3: download missing papers using their now found s2ids
    # make_download_found_s2papers()
    # save_combined_found_s2papers()

    combined_found_s2papers = u_json.load_json(COMBINED_FOUND_S2PAPERS_FN)
    print(len(combined_found_s2papers))
