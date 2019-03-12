import json
import os
import csv

# ON GIT

# systems_papers_directory = "/data/sys-papers/"
systems_papers_directory = "../"

data_directory     = systems_papers_directory+"authors/data/"
authors_directory  = data_directory+"authors/"
conf_directory     = data_directory+"conf/"

features_directory = systems_papers_directory+"authors/features/"

papers_directory   = systems_papers_directory + "sys-papers/"

script_directory   = "../script/"

persons_directory  = systems_papers_directory + "persons/"

# OFF GIT

paperdata_directory = "/home/blancheh/"

semantic_scholar_dir            = paperdata_directory + "semsch/"
semantic_scholar_proccessed_dir = "../../data/"
semantic_scholar_tmp_dir        = semantic_scholar_dir + "tmp/"

papergroups_directory = paperdata_directory + "papers/"
groupA_directory      = papergroups_directory + "A/"
groupB_directory      = papergroups_directory + "B/"

################################################################################
# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###  #
################################################################################

def fileToString(path):
    try:
        with open(path, 'r') as file:
            s = ""
            for line in file: s += line
            return s
    except:
        print("[!] Problem reading file: " + path)

def getJSONData(path):
    data_raw = fileToString(path)
    return json.loads(data_raw)

def getJSONFilenames(directory):
    return filter(lambda x : x.endswith(".json") and not x.endswith("template.json"), os.listdir(directory))

def getConferenceFilenames():
    ls = list(getJSONFilenames(conf_directory))
    if "allConferencePapers.json" in ls: ls.remove("allConferencePapers.json")
    return ls

def getConferenceNames():
    ls = list(getJSONFilenames(conf_directory))
    if "allConferencePapers.json" in ls: ls.remove("allConferencePapers.json")
    ls = map(lambda s: s.replace(".json",""), ls)
    return ls

def getConference(conf_name):
    return getJSONData(conf_directory+conf_name+".json")

def getAllConferences():
    for conf_name in getConferenceNames():
        yield getConference(conf_name)

# get json file in data/conf/
def getPapers(conf_filename):
    return getJSONData(conf_directory+conf_filename)

# get json file in data/authors/
def getAuthors(conf_filename):
    return getJSONData(authors_directory+conf_filename)

# get combined json of all papers in
# original conference data
def getAllConferencePapers():
    return getJSONData(conf_directory+"allConferencePapers.json")

if __name__ == "__main__":
    # print(list(getConferenceNames()))
    print(list(getConference("ASPLOS")["papers"])[0]["title"])
