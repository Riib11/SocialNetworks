import utils.json as u_json
import utils.csv as u_csv

PARENT_DIR = "conferences/"
DATA_DIR   = PARENT_DIR + "data/"

S2ID_KEY_OLD_FN = DATA_DIR + "s2id_key_old.json"
KEY_S2ID_ADD_FN = DATA_DIR + "missing_key_to_found_s2id.json"
S2ID_KEY_NEW_FN = DATA_DIR + "s2id_key.json"
S2ID_KEY_NEW_CSV_FN = S2ID_KEY_NEW_FN.replace(".json", ".csv")

# old
s2id_key_old = u_json.load_json(S2ID_KEY_OLD_FN)

# add
key_s2id_add = u_json.load_json(KEY_S2ID_ADD_FN)
s2id_key_add = { v:k for k,v in key_s2id_add.items() if v != None }

# new
s2id_key_new = { k:v for k,v in s2id_key_old.items() }

for s2id, key in s2id_key_add.items():
    s2id_key_new[s2id] = key

# save new
u_json.dump_json(s2id_key_new, S2ID_KEY_NEW_FN)
u_csv.dump_csv(s2id_key_new, S2ID_KEY_NEW_CSV_FN)
