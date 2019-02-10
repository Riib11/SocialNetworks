import utils.shared_utils as utils
import papers.paper_features as p_features
import os
import json
from tqdm import tqdm

# src: https://stackoverflow.com/questions/2460177/edit-distance-in-python
def editdist(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

class S2Search:

    def __init__(self, dirname, thresholds, debug=False):
        self.dirname = dirname
        self.thresholds = thresholds
        self.debug = debug
        self.entries = []

    def loadfile(self, filename):
        file = open(self.dirname + filename, "r+", encoding="utf-8")
        self.entries = json.load(file)
        file.close()

    def cleanName(self, name):
        name = name.split()
        if len(name) == 1: return name[0]
        return name[0][0:1].capitalize() + " " + name[1]

    def query(self,authors,title,year):
        filenames = os.listdir(self.dirname)
        possibles = [] # entry objects
        distances = [] # total distance score for each object

        threshold = 0
        if "author" in self.thresholds: threshold += self.thresholds["author"]
        if "title"  in self.thresholds: threshold += self.thresholds["title"]

        for filename in tqdm(filenames):
            if not filename.endswith(".json"): continue
            self.loadfile(filename)
            for entry in tqdm(self.entries):
                year_dist, title_dist, auth_dist = 0,0,0
                # check if year is within threshold
                if year and "year" in entry:
                    year_dist = editdist(str(entry["year"])[0:4],year[0:4])
                    if year_dist >= self.thresholds["year"]: continue                
                # check if title is within threshold
                if title and "title" in entry:
                    title_dist = editdist(entry["title"],title)
                    if title_dist >= self.thresholds["title"]: continue
                # check if authors are within threshold
                if authors and "authors" in entry: # TODO: check each author individually?
                    ds = [ editdist(
                                self.cleanName(auth1["name"]),
                                self.cleanName(a2))
                            for auth1 in entry["authors"]
                            for a2 in authors ]
                    if len(ds) == 0: continue
                    auth_dist += min(ds)
                    if auth_dist >= self.thresholds["author"]: continue
                # add to possibilities
                possibles.append(entry)
                distances.append(year_dist + title_dist + auth_dist)

        if len(possibles)==0: raise Exception("Didn't find semantic scholar query for paper with title '" + title + "'")

        # get min
        i_min = 0
        dist_min = 1 + sum([ v for v in self.thresholds.values() ])
        for i in range(len(distances)):
            d = distances[i]
            if d < dist_min:
                dist_min = d
                i_min = i
        
        return possibles[i_min], dist_min