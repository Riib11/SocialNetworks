PARENT_DIR   = "find_missing/"
MISSING_1_FN = PARENT_DIR + "find_missing_papers_result.txt"
MISSING_2_FN = PARENT_DIR + "find_missing_papers_result_2.txt"
PARTIAL_FN   = PARENT_DIR + "partial_titles.txt"

with open(MISSING_1_FN, "r+") as file: missing_1_titles = [ line.strip() for line in file ]
with open(MISSING_2_FN, "r+") as file: missing_2_titles = [ line.strip() for line in file ]

partial_titles = [ t for t in missing_1_titles if not t in missing_2_titles ]
with open(PARTIAL_FN, "w+") as file: [ file.write(t+"\n") for t in partial_titles ]
