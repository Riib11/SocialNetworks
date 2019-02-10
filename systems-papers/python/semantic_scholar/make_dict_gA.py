import semantic_scholar.s2data as s2data
import utils.shared_utils as utils
from tqdm import tqdm

gA_dict = {}
for c in tqdm(s2data.get_gA()): gA_dict[ c["id"] ] = c
utils.save_json_file( s2data.dict_gA_fn, gA_dict )
