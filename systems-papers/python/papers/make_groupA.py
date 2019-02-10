import xml.etree.ElementTree as ET
import os
from tqdm import tqdm
import json

import papers.paper_data as paper_data
import utils.data as data
import utils.xml as xml

papers_directory = data.paperdata_directory
papers_filenames = paper_data.getPaperFilenames_XML()

gA = []

for fn in tqdm(papers_filenames):
    path = papers_directory + fn
    try:
        root = xml.parseXML(path)
        j = xml.XML_to_JSON(root)
        j["error"] = False
        j["fn"] = fn
        gA.append(j)
    except:
        j = {"error":True , "fn":fn}
        gA.append(j)

json.dump(gA, open(paper_data.gA_fn, "w+"))