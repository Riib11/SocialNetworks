import json

with open("../gA_all_dict_old_1.json", "r+") as file:
  gA_dict = json.load(file)

with open("../found_all.json", "r+") as file:
  gA_found_dict = json.load(file)

gA_all_dict = { k:v for k,v in gA_dict.items() }

print("old:", len(gA_dict))
print("add:", len(gA_found_dict))

for p_id, p in gA_found_dict.items(): gA_all_dict[p_id] = p

print("new:", len(gA_all_dict))
print("dif:", len(gA_all_dict) - len(gA_dict))

with open("../gA_all_dict.json", "w+") as file:
  json.dump(gA_all_dict, file, indent=2)
