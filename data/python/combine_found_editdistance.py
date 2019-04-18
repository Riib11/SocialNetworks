import json

GA_DICT_1_FN = "../gA_all_dict.json"

FOUND_ED_FN = "../found_all_editdistance.json"
GA_DICT_2_FN = "../gA_dict_2.json"

gA_dict_1 = json.load(open(GA_DICT_1_FN, "r+"))
found_ed_dict = json.load(open(FOUND_ED_FN, "r+"))
prev_total = len(gA_dict_1)
add_total = len(found_ed_dict)

gA_dict_2 = gA_dict_1
for s2id, paper in found_ed_dict.items(): gA_dict_2[s2id] = paper
new_total = len(gA_dict_2)

json.dump(gA_dict_2, open(GA_DICT_2_FN, "w+"))

print("prev total:", prev_total)
print("    to add:", add_total)
print("     added:", new_total - prev_total)
print(" new total:", new_total)
