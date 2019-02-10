import semantic_scholar.s2data as s2data
from utils.data import semantic_scholar_proccessed_dir
import json
from tqdm import tqdm

# look in our database at the papers in group A that have no outCitations, and then add an entry of them to the citersdict with the list of outCitations that i find

# find found papers in Group A that have empty outCitations
citersdict = s2data.getCitersDict()
print(citersdict.items()[0])
quit()
zeroOutcites = [
    p for p in citersdict.items()
    if (
        "outCitations" in p
        and len(p["outCitations"])==0
    )
]

print("number of papers with 0 outcites:",len(zeroOutcites))

# papers
papers = data.getAllConferencePapers()

results = []
print("finding original papers:")
for p0 in tqdm(zeroOutcites):
    p0_title = p0["title"]
    # find paper in original data,
    # to get list of citations
    for p in papers:
        # TODO: make sure that the `==` is
        #       going to be the right relation here
        if "title" in p and p["title"] == p0_title:
            results.append(p)
            break