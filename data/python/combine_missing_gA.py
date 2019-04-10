import json

with open("../gA.json",         "r+") as file: gA_list         = json.load(file)
with open("../missing_gA.json", "r+") as file: gA_missing_list = json.load(file)

gA_ids = [ p["id"] for p in gA_list ]

gA_missing_new_list = [ p for p in gA_missing_list if not p["id"] in gA_ids ]

gA_all = gA_list + gA_missing_new_list
gA_all_dict = { p["id"] : p for p in gA_all }

print("old:", len(gA_list))
print("new:", len(gA_all))
print("dif:", len(gA_all) - len(gA_list))

with open("../gA_all.json", "w+")      as file: json.dump(gA_all,      file)
with open("../gA_all_dict.json", "w+") as file: json.dump(gA_all_dict, file)
