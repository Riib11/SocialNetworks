with open("find_missing/found_ids.txt") as file:
  found_ids = [ line.strip() for line in file ]

with open("find_missing/grep_found.sh", "w+") as file:
  file.write("# !/bin/bash\n")
  for id in found_ids:
    if id != "!":
      file.write('grep "\\"id\\": \\"{0}\\"" /data/sys-papers/semsch/s2-corpus-*.json > /data/sys-papers/semsch/tmp/gA_found\n'.format(id))
