import semantic_scholar.s2data as s2data

citeds = s2data.getCitedsDict()
citeds = s2data.getCitersDict()

notfound = []
for paper in citers.values():
    outcites = paper["outCitations"] if "outCitations" in paper else False
    if outcites:
        for id in outcites:
            if not id in citeds.keys():
                notfound.append(id)

json.dump(open(s2data.missed_outcites_fn, "w+"))