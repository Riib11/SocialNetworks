import csv

def dict_to_csv(d, file):
  writer = csv.write()
  writer.writerow()

  writer = csv.writer(file)
  node_ids = list(self.graph.nodes())
  writer.writerow([""] + node_ids)
  for node_i in range(len(node_ids)):
    node_id = node_ids[node_i]
    adjmat_row = list(map(str,adjmat_list[node_i]))
    writer.writerow([node_id] + adjmat_row)
