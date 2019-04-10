import json

with open("../gA_all_old.json",         "r+") as file: gA_list       = json.load(file)
with open("../found_all_gA_dict.json", "r+") as file: gA_found_dict = json.load(file)

gA_ids = [ p["id"] for p in gA_list ]

gA_found_list = [ p for p_id, p in gA_found_dict.items() if not p_id in gA_ids ]

gA_all = gA_list + gA_found_list
gA_all_dict = { (p["id"] if "id" in p else p["paperId"]) : p for p in gA_all }

print("old:", len(gA_list))
print("new:", len(gA_all))
print("dif:", len(gA_all) - len(gA_list))

with open("../gA_all.json", "w+")      as file: json.dump(gA_all,      file)
with open("../gA_all_dict.json", "w+") as file: json.dump(gA_all_dict, file)
