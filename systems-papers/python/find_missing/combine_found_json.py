import json
import glob

with open("find_missing/found_all.json", "w+") as file:
  d = {}
  for fn in glob.glob("find_missing/found_json/*"):
    paper = json.load(open(fn, "r+"))
    p_id = paper["paperId"]
    d[p_id] = paper
    # expected_id = fn.split("/")[-1]
    # if "38a7e8ef5b18bd4601bfbeedc0e8dcfe07d28620" == p_id: print(fn)
  json.dump(d, file, indent=4, sort_keys=True)
