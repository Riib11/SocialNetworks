import json
import glob

with open("find_missing/found_all.json", "w+") as file:
  d = {}
  for fn in glob.glob("find_missing/found_json/*"):
    paper = json.load(open(fn, "r+"))
    p_id = paper["id"] if "id" in paper else paper["paperId"]
    d[p_id] = paper
  json.dump(d, file, indent=4, sort_keys=True)
