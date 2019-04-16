import json

with open("../gA_all_dict.json") as file: s2id_paper = json.load(file)

print("len(s2id_paper) = ", len(s2id_paper))

mismatches = []
for s2id, paper in s2id_paper.items():
  if s2id != paper["id"]: mismatches.append(paper)

print("len(mismatches) =", len(mismatches))

quit()

duplicates = []

def match(s1, s2): return s1.lower() == s2.lower()

for s2id, paper in s2id_paper.items():
  c = len([ 0 for s2id_, paper_ in s2id_paper.items()
    if match(paper["title"], paper_["title"]) and not (print(s2id, s2id_) if s2id != s2id_ else None) ])
  if c != 1: duplicates.append(paper)

print("len(duplicates) = ", len(duplicates))

print("difference =", len(s2id_paper) - len(duplicates))
