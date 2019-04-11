import json

bad_titles_list_fn = "find_missing/find_missing_papers_result_2.txt"
good_ids_list_fn   = "find_missing/found_ids.txt"
bad_to_id          = "find_missing/bad_title_to_id.json"

with open(bad_titles_list_fn, "r+") as file:
  bad_titles_list = [ line.strip() for line in file ]

with open(good_ids_list_fn, "r+") as file:
  good_ids_list = [ line.strip() for line in file ]

d = {}
for bad_title, good_id in zip(bad_titles_list, good_ids_list):
  if good_id != "!":
    d[bad_title] = good_id
  else:
    d[bad_title] = None

with open(bad_to_id, "w+") as file: json.dump(d, file, indent=4)
