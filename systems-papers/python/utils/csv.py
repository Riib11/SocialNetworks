import csv
import utils.debug as debug
from tqdm import tqdm

def dump_csv(d, fn, headers=None):
    debug.log("writing csv to file: "+fn)
    with open(fn, "w+") as file:
        writer = csv.writer(file, delimiter=',')
        if headers: writer.writerow(headers)
        for k,v in tqdm(d.items()): writer.writerow([k,v])

# def dict_to_csv(d, file):
#   writer = csv.write()
#   writer.writerow()
#
#   writer = csv.writer(file)
#   node_ids = list(self.graph.nodes())
#   writer.writerow([""] + node_ids)
#   for node_i in range(len(node_ids)):
#     node_id = node_ids[node_i]
#     adjmat_row = list(map(str,adjmat_list[node_i]))
#     writer.writerow([node_id] + adjmat_row)

if __name__ == "__main__":
    d = {"hello": "world"}
    dict_to_csv(d, "/Users/Henry/Downloads/test-dict.csv")
