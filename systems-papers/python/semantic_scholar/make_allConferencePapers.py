import utils.data as data
import json

papers = []

cfns = data.getConferenceFilenames()
for cfn in cfns:
    papers += data.getPapers(cfn)["papers"]

json.dump(papers, open(data.conf_directory+"allConferencePapers.json","w+"))