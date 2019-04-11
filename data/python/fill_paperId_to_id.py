import json

gA_all_dict_fn = "../gA_all_dict.json"
gA_all_list_fn = "../gA_all.json"

with open(gA_all_dict_fn, "r+") as file: gA_all_dict = json.load(file)
with open(gA_all_list_fn, "r+") as file: gA_all_list = json.load(file)

for p_id, p in gA_all_dict.items():
  if not "id" in p: p["id"] = p_id

for p in gA_all_list:
  if not "id" in p: p["id"] = p["paperId"]

with open(gA_all_dict_fn, "r+") as file: json.dump(gA_all_dict, file)
with open(gA_all_list_fn, "r+") as file: json.dump(gA_all_list, file)
