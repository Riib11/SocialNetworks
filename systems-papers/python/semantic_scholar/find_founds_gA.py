import semantic_scholar.s2data as s2data
import utils.data as u_data
import utils.strings as u_strings

import json
from tqdm import tqdm

# levenshtein threshold
threshold = 5

# dictionary of papers not found in SS corpus
# keyed by title, valued by paper (from autors/data)
missings = s2data.get_missing_gA()

# load all the corpus data
corpi = [ json.load(open(
    u_data.semantic_scholar_dir+"s2-corpus-" + str(ten)+str(one) + ".json" ))
    for ten in range(0,4)
    for one in range(0,10) ]

print("finished loading the corpi")

found_originals = []
found_papers   = []

# for each paper,
for title, paper in missings.items():
    # check each corpus paper
    for corpus in corpi:
        for p in corpus:
            if "title" in p:
                if u_strings.levenshtein( title , p["title"] ) < threshold:
                    found_originals.append(paper)
                    found__papers.append(p)

print("finished looking the titles")
print("looked for " + len(missing) + " papers")
print("found " + len(found_originals) + " papers")

json.dump(found_originals, open(u_data.semantic_scholar_proccessed_dir + "found_originals_gA.json", "w+"))
json.dump(found_papers, open(u_data.semantic_scholar_proccessed_dir +  "found_gA.json","w+"))

print("done!")
