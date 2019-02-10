import xml.etree.ElementTree as ET
import os

directory = "/data/sys-papers/"
filenames = [ fn for fn in os.listdir(directory) if fn.endswith("cermxml") ]

total_citations_count = 0

for fn in filenames:
    tree = ET.parse(directory + fn)
    root = tree.getroot()
    for root_child in root:
        # back
        if root_child.tag == "back":
            back = root_child
            # ref-list
            for back_child in back:
                if back_child.tag == "ref-list":
                    reflist = back_child
                    total_citations_count += len(reflist)

print("total citations count:", total_citations_count)