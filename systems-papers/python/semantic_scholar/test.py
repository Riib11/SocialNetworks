import semantic_scholar.s2data as s2data
import utils.data as u_data

citers = s2data.getCitersDict()

no_outcites = 0
for c in citers.values():
    if not "outCitations" in c:
        no_outcites += 1
    else:
        if len(c["outCitations"]) == 0:
            no_outcites += 1
print(no_outcites)


# print(len(citers.keys())) # 1566

# cfns = [ fn for fn in u_data.getConferenceFilenames() ]
# total = 0
# for cfn in cfns:
#     data = u_data.getPapers(cfn)
#     papers = data["papers"]
#     total += len(papers)

# print(total) # 2439