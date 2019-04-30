import utils.shared_utils as utils
from utils.data import semantic_scholar_proccessed_dir, semantic_scholar_tmp_dir

# Divided Raw Data (lists)

make_grep_gA_cnf_fn = lambda i: semantic_scholar_tmp_dir + "gA_cfn_" + str(i)
make_grep_gB_sec_fn = lambda i: semantic_scholar_tmp_dir + "gB_sec_" + str(i)
make_grep_gA_mis_fn = lambda i: semantic_scholar_tmp_dir + "gA_missing_" + str(i)

# Raw Data (list)

# gA_fn = semantic_scholar_proccessed_dir + "gA.json"
# gA_fn = semantic_scholar_proccessed_dir + "gA_all.json"
gA_fn = semantic_scholar_proccessed_dir + "gA_dict_04-28.json"
get_gA = lambda: utils.load_json_file(gA_fn)

gB_fn = semantic_scholar_proccessed_dir + "gB.json"
get_gB = lambda: utils.load_json_file(gB_fn)

# Processed data (dict)

dict_gA_old_fn = semantic_scholar_proccessed_dir + "dict_gA.json"
get_dict_gA_old = lambda: utils.load_json_file(dict_gA_old_fn)

dict_gA_fn = semantic_scholar_proccessed_dir + "gA_dict_2.json"
get_dict_gA = lambda: utils.load_json_file(dict_gA_fn)

dict_gB_fn = semantic_scholar_proccessed_dir + "dict_gB.json"
get_dict_gB = lambda: utils.load_json_file(dict_gB_fn)

# Just Ids (list)

list_gB_fn = semantic_scholar_proccessed_dir + "list_gB.json"
get_list_gB = lambda: utils.load_json_file(list_gB_fn)

# Missing

missing_gA_fn = semantic_scholar_proccessed_dir + "missing_gA.json"
get_missing_gA = lambda: utils.load_json_file(missing_gA_fn)

# TODO
missing_gB_fn = semantic_scholar_proccessed_dir + "missing_gB.json"
get_missing_gB = lambda: utils.load_json_file(missing_gB_fn)

# Missed

missed_outcites_fn = semantic_scholar_proccessed_dir + "missed_outcites.json"
get_missed_outcites = lambda: utils.load_json_file(missed_outcites_fn)
