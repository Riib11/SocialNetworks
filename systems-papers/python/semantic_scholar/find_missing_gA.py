import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm
import re
import math
import json

#
# Goal:
#   find the citers that weren't grepped into `citersdict`
#

# DEPRECATED
# compile all of the s2 corpus files
# together into one big megafile, so its
# faster to grep it for titles
#

gA_dict = s2data.get_dict_gA()
gA_string = str(gA_dict)

#
# search for all the papers
#

missing = {}

# loop through titles of papers
cfns = [ fn for fn in u_data.getConferenceFilenames() ]
last_i = len(cfns) - 1

# start index
i = 0

cfns = cfns[i:] # already did the first 43

for cfn in tqdm(cfns):
    
    cname = cfn.replace(".json","")
    data = u_data.getPapers(cfn)
    papers = data["papers"]

    for p in papers:
        title = p["title"]
        string = "'title': '"+title+"'"
        string = re.escape(string)
        find = re.search(string, gA_string, re.IGNORECASE)
        if find==None: missing[p["title"]] = p

json.dump(missing, open(s2data.missing_gA_fn,"w+"))
