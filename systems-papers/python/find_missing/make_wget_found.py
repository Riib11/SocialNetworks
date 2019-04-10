with open("find_missing/found_ids.txt") as file:
  found_ids = [ line.strip() for line in file ]

with open("find_missing/wget_found.sh", "w+") as file:
  file.write("# !/bin/bash\n")
  for f_id in found_ids:
    if f_id != "!":
      file.write(
        "wget -O \"found_json/{f_id}\" \"https://api.semanticscholar.org/v1/paper/{f_id}\"\n"\
        .format(f_id=f_id))
