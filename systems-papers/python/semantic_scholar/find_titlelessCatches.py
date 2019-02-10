import semantic_scholar.s2data as s2data
from utils.data import semantic_scholar_proccessed_dir
import json

# find the results stores in `citersdict.json` that don't have titles.

# all found entries of group A
citersdict = s2data.getCitersDict()
# all found titleless entries of group A
targets = [ p for p in citersdict.items() if not "title" in p ]
# output targets to appropriate folder in semantic scholar data folder
fn = semantic_scholar_proccessed_dir+"titleless_catches.json"
json.dump(targets,fn)
print("wrote targets to " + fn)