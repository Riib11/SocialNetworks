"""

TODO

"""

# utilities
import sys
import os
import json
import numpy as np
import utils.shared_utils as utils
import utils.conf_utils as conf_utils
import utils.colors as u_colors
from tqdm import tqdm

# modules
import utils.data as u_data
import semantic_scholar.s2data as s2data

################################################################
print("[#] Loading Data:")

gA = s2data.get_dict_gA()
gB = s2data.get_dict_gB()

for x in gA.items():
    print(x)
    exit()

################################################################
print("[#] Analyzing gA Data:")

statistics = {}

def increment_entry(d, k, i=1):
    k = k.lower()
    if not k in d: d[k] = 0
    d[k] += i


statistics["gA"] = {
    "outCitations": [],
    "titlewords": {},
    "author_collaborations": {},
    "paper_authors": []
}
gA_statistics = statistics["gA"]

statistics["gAconfs"] = {
    "inCitaitons": []
}
 
for paper in tqdm(gA.values()):
    # citation count
    outcitationcount = len(paper["outCitations"])
    gA_statistics["outCitations"].append(outcitationcount)
    # author collaborations
    author_ids = []
    for a in paper["authors"]:
        if "ids" in a and len(a["ids"]) > 0:
            author_ids.append(a["ids"][0])

    for author_id in author_ids:
        increment_entry(gA_statistics["author_collaborations"],
            author_id, len(author_ids)-1)

    gA_statistics["paper_authors"].append(len(author_ids))
    if author_ids == []: print(paper["title"])

    # title words
    titlewords = paper["title"].split()
    for word in titlewords:
        increment_entry(gA_statistics["titlewords"],word)

################################################################
print("[#] Analyzing gB Data:")

statistics["gB"] = {
    "inCitations": [],
    "inCitationsRate": [],
    "titlewords": {},
    "years": []
}
gB_statistics = statistics["gB"]

for paper in tqdm(gB.values()):
    if not "year" in paper: continue
    # citation count
    incitationcount = len(paper["inCitations"])
    gB_statistics["inCitations"].append(incitationcount)
    gB_statistics["inCitationsRate"].append(
        incitationcount/(1 + 2018 - paper["year"]))
    # title words
    titlewords = paper["title"].split()
    for word in titlewords:
       increment_entry(gB_statistics["titlewords"],word)
    # years
    gB_statistics["years"].append(paper["year"])

################################################################
print("[#] Writing Results:")

with open("../statistics/papers_statistics.txt","w+") as file:
    #
    #
    file.write("################################\n")
    file.write("gA statistics:\n")
    #
    data = gA_statistics["outCitations"]
    file.write("  + outCitation counts:\n")
    file.write("  |     mean : "+str(np.mean(data))+"\n")
    file.write("  |   median : "+str(np.median(data))+"\n")
    file.write("  |      std : "+str(np.std(data))+"\n")
    #
    data = list(gA_statistics["author_collaborations"].values())
    file.write("  + author collaborations\n")
    file.write("  |     mean : "+str(np.mean(data))+"\n")
    file.write("  |   median : "+str(np.median(data))+"\n")
    file.write("  |      std : "+str(np.std(data))+"\n")
    #
    data = list(gA_statistics["paper_authors"])
    file.write("  + paper authors\n")
    file.write("  |     mean : "+str(np.mean(data))+"\n")
    file.write("  |   median : "+str(np.median(data))+"\n")
    file.write("  |      std : "+str(np.std(data))+"\n")
    #
    file.write("  + top couple title words:\n")
    def get(i): return i[1]
    titlewords = sorted(list(gA_statistics["titlewords"].items()), key=get)
    titlewords_len = len(titlewords)
    for i in range(1,100+1): file.write("  |   "+str(i)+". ["+str(np.round(titlewords[-i][1]/titlewords_len, 3))+"] "+titlewords[-i][0]+"\n")

    #
    #
    file.write("################################\n")
    file.write("gB statistics:\n")
    #
    data = gB_statistics["inCitations"]
    file.write("  + inCitation/year counts:\n")
    file.write("  |     mean : "+str(np.mean(data))+"\n")
    file.write("  |   median : "+str(np.median(data))+"\n")
    file.write("  |      std : "+str(np.std(data))+"\n")
    #
    data = gB_statistics["years"]
    file.write("  + publish years:\n")
    file.write("  |     mean : "+str(np.mean(data))+"\n")
    file.write("  |   median : "+str(np.median(data))+"\n")
    file.write("  |      std : "+str(np.std(data))+"\n")

    file.write("  + top couple title words:\n")
    titlewords = sorted(list(gB_statistics["titlewords"].items()), key=get)
    titlewords_len = len(titlewords)
    for i in range(1,100+1): file.write("  |   "+str(i)+". ["+str(np.round(titlewords[-i][1]/titlewords_len, 3))+"] "+titlewords[-i][0]+"\n")

    # dump to json
    json.dump(statistics,
        open("../statistics/papers_statistics.json", "w+"))
