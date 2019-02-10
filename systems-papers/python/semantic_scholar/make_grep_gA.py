import semantic_scholar.s2data as s2data
import utils.data as u_data
from tqdm import tqdm
import math

fn_grep_gA = u_data.script_directory+"grep_gA.sh"

# script
grep_gA = open(fn_grep_gA,"w+")
grep_gA.write("#!/bin/bash\n\n")

# loop through titles of papers
cfns = [ fn for fn in u_data.getConferenceFilenames() ]
# cfns = cfns[12:13]

per_part = 1                            # conferences per partition
parts = math.ceil(len(cfns)/per_part)   # number of partitions
part_i = 0                              # index within partition
part_j = 0                              # index of partition
i = 0

checks = ""

for cfn in tqdm(cfns):
    
    cname = cfn.replace(".json","")
    data = u_data.getPapers(cfn)
    papers = data["papers"]

    cmd = "\n"

    if part_i == 0:
        cmd += 'echo "starting section ' + str(part_j) + '"'
        cmd += ' & grep -i -h'
    else:
        cmd += ' & grep -i -h'

    for p in papers:
        title = p["title"].replace('"','\\"')
        cmd += " -e " + "\"\\\"title\\\":\\\"" + title + "\\\"\""

    cmd += ' ' + u_data.semantic_scholar_dir + 's2-corpus-*.json'

    datafile_fn = s2data.make_grep_gA_cnf_fn(i)

    # write finds to file
    cmd += ' > ' + datafile_fn

    # log the files that have problems
    # which is run after all the greps are done
    checks += '\n\n'
    checks += "count=$(wc -l < " + datafile_fn + ")\n"
    checks += "target='" + str(len(papers)) + "'\n"
    checks += "if [ $count != $target ]; then\n"
    checks += "  echo " + datafile_fn + " : target for " + data["key"] + " = $target , count=$count > " + datafile_fn+"_errors " + "\nfi\n"

    # write cmd
    grep_gA.write(cmd)

    # increment
    i      += 1
    part_i += 1
    if part_i == per_part:
        part_i = 0
        part_j += 1


grep_gA.write(checks)

grep_gA.close()
