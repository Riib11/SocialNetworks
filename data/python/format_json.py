import json
import sys

fn = sys.argv[1]
with open(fn, "r+") as file: json_original = json.load(file)
with open(fn, "w+") as file: json.dump(json_original, file, indent=4, sort_keys=True)
