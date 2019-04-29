import json

##################################################
gA_old_fn = "../gA_all_dict.json"
gA_add_fn = "../combined_found_s2papers.json"
##################################################
gA_new_fn = "../gA_dict_04-28.json"

#############################################################################################################################

def load_json(fn):
    with open(fn, "r+") as file: return json.load(file)

def dump_json(d, fn):
    with open(fn, "w+") as file: json.dump(d, file, indent=2)

#############################################################################################################################

gA_old = load_json(gA_old_fn)
gA_add = load_json(gA_add_fn)

gA_new = { k:v for k,v in gA_old.items() }

print("old:", len(gA_old))
print("add:", len(gA_add))

for k,v in gA_add.items(): gA_new[k] = v

print("new:", len(gA_new))
print("dif:", len(gA_new) - len(gA_old))

dump_json(gA_new, gA_new_fn)
