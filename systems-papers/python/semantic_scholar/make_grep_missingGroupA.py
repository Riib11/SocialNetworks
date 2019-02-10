import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm
import math

filename = u_data.systems_papers_directory+"script/grep_missing_groupA.sh"

file         = open(filename,"w+")
paper_titles = list(s2data.getMissingGroupA().keys())

per_part     = 8                               # processes per partition
parts        = math.ceil(len(papers)/per_part) # number of partitions

paper_parts = []
for i in range(len(paper_titles)):
    if i%per_part==0: paper_parts.append([]) # start of partition
    paper_parts[-1].append(paper_titles[i])  # add this paper title

for paper_part_i in range(len(paper_parts)):

    paper_part = paper_parts[paper_part_i]

    cmd = 'echo starting part ' + str(paper_part_i) + '\n'
    cmd += 'grep -h -i'

    for paper_title in paper_part:
        paper_title = paper_title.replace('"','\\"')
        cmd += ' -e "' + paper_title + '"'

    cmd += ' ' + u_data.semantic_scholar_dir + 's2-corpus-*.json'
    cmd += ' > ' + s2data.makeGrepMissingGroupAFn(paper_part_i)

    # write cmd
    file.write(cmd)

file.write(
    '\n\necho "[Done] Don\'t forget to concat the output and format it and everything!"')

file.close()
