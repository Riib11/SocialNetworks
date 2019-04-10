parent_dir    = "find_missing/"
found_urls_fn = parent_dir + "found_urls.txt"
found_ids_fn  = parent_dir + "found_ids.txt"

with open(found_urls_fn, "r+") as file:
  found_urls = [ line.strip() for line in file ]

found_ids = []
for url in found_urls:
  id = url.split("/")[-1] if url != "!" else "!"
  found_ids.append(id)

with open(found_ids_fn, "w+") as file:
  file.write("\n".join(found_ids))
