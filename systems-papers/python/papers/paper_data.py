import utils.data as data
import json
import os

def getPaperFilenames_XML():
    return [ fn
             for fn in os.listdir(data.paperdata_directory)
             if fn.endswith(".cermxml") ]


groupA_fn = data.groupA_directory+"gA.json"
def getGroupA(): return json.load(open(groupA_fn))

groupB_fn = data.groupB_directory+"gB.json"
def getGroupB(): return json.load(open(groupB_fn))
