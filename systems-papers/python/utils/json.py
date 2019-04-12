# import pickle
import json

def load_json(fn):
  with open(fn, "r+") as file: return json.load(file)

def dump_json(obj, fn):
  with open(fn, "w+") as file: json.dump(obj, file, indent=4)
