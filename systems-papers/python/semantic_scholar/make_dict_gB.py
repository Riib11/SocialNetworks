import semantic_scholar.s2data as s2data
import data.shared_utils as utils

citedsdict = {}

for c in s2data.getCiteds():
    citedsdict[ c["id"] ] = c

utils.save_json_file( s2data.citedsdict_fn, citedsdict )