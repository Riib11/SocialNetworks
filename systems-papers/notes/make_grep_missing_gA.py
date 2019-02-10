with open("missing_ids_gA.txt", "r+") as ids:
    with open("grep_missing_gA.sh", "w+") as file:
        batches = []
        ids = [id.strip() for id in ids]
        for i in range(len(ids)):
            if i % 15 == 0:
                batches.append([])
            batches[-1].append(ids[i])

        for batch in batches:
            s = "grep -h "
            for id in batch:
                s += "-e '\"id\":\"" + id + "\"' "
            s += "/data/sys-papers/semsch/*.json >> /home/blancheh/semsch/processed/missing_gA.json"
            s += "\n"
            file.write(s)

