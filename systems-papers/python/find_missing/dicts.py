import utils.json as json

PARENT_DIR     = "find_missing/"
BAD_TO_GOOD_FN = PARENT_DIR + "bad_to_good.json"

get_bad_to_good = lambda: json.load_json(BAD_TO_GOOD_FN)
