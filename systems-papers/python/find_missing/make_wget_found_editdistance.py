DATA_DIR = "find_missing/data/"
MISSING_RAWTITLES_ED_IDS_FN = DATA_DIR + "missing_rawtitles_editdistance_ids.txt"
WGET_FOUND_ED_FN = "find_missing/wget_found_editdistance.sh"
FOUND_JSON_ED_DIR = "data/json_editdistance/"

with open(MISSING_RAWTITLES_ED_IDS_FN) as file:
  found_ids = []
  for line in file:
    line = line.strip()
    if line != "!": found_ids.append(line)

print(len(found_ids))

with open(WGET_FOUND_ED_FN, "w+") as file:
  file.write("# !/bin/bash\n")
  for f_id in found_ids:
    file.write(
      "wget -O \"{wget_dir}{s2id}\" \"https://api.semanticscholar.org/v1/paper/{s2id}\"\n"\
      .format(
        wget_dir = FOUND_JSON_ED_DIR,
        s2id     = f_id
      ))
