import xml.etree.ElementTree as ET
import os
from tqdm import tqdm

import papers.paper_data as paper_data
import utils.data as data
import utils.xml as xml

total_citations_count = 0
total_errors_count = 0

papers_directory = "/data/sys-papers/sys-papers/"
papers_filenames = paper_data.getPaperFilenames_XML()
print("len(groupA) =",len(papers_filenames))

for fn in tqdm(papers_filenames):
    path = papers_directory + fn
    root = xml.parseXML(path, do_raise=False)
    try:
        reflist = xml.getDescendantByTagPath(root, ["back","ref-list"])
        total_citations_count += len(reflist)
    except:
        total_errors_count += 1

print("len(groupB)", total_citations_count)
print("total groupA errors:", total_errors_count)
