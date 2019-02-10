import semantic_scholar.s2data as s2data
import utils.shared_utils as utils
from itertools import chain
from tqdm import tqdm

# set of ids
ids = set({})
for c in tqdm(s2data.get_gA()):
    # get the id's of the citeds
    if "outCitations" in c: ids = set(chain(c["outCitations"],ids))

# convert back to list
ids = list(ids)

# save
utils.save_json_file( s2data.list_gB_fn , ids )