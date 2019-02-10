import pickle

def load_json(filename):
  with open(filename, "rb") as file: return pickle.load(file)

def dump_json(x, filename):
  with open(filename, "wb+") as file: pickle.dump(x, file)
