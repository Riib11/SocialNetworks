import semantic_scholar.s2data as s2data
import utils.shared_utils as utils
import utils.data as u_data
import math
from tqdm import tqdm

fn_grep_gB = "../script/grep_gB.sh"
grep_gB = open(fn_grep_gB,"w+")
grep_gB.write("#!/bin/bash\n\n")

# list of cited ids
list_gB = s2data.get_list_gB()

# organize into grep-sections
per_grep = 20
greps_n = math.ceil(len(list_gB)/per_grep)

greps = []
i = 0
for pid in tqdm(list_gB):
    if i == 0: greps.append([])
    greps[-1].append(pid)
    i += 1
    if i == per_grep: i = 0

# organize into parallel parts
per_part = 1
parts_n = math.ceil(greps_n/per_part)
part_i = 0 # index of partition
part_j = 0 # index within partition

i = 0
i_start = 588
for grep in tqdm(greps):

    cmd = ''

    if i >= i_start:

        if part_i == 0:
            cmd += '\necho "starting section ' + str(i) + '"'
            cmd += ' & grep -h'
        else:
            cmd += ' & grep -h'

        for pid in grep:
            cmd += " -e " + "\"" + "\\\"id\\\"" + ":" + "\\\"" + pid + "\\\"" + "\""

        cmd += ' ' + u_data.semantic_scholar_dir + 's2-corpus-*.json'
        cmd += ' > ' + s2data.make_grep_gB_sec_fn(i)

        grep_gB.write(cmd)

    # increment
    i      += 1
    part_i += 1
    if part_i == per_part:
        part_i = 0
        part_j += 1
