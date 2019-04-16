import csv

VERSION = "A1"

"""
save_correlations_csv:
  each column of csv is an attribute
  each row of csv is an author (node)

keys : [ attr_key ]
data : author_name => { attr_key : attr_val }
"""
def save_correlations_csv(keys, data, iso_comp, DIR_DATA):
  if iso_comp:
    fn = DIR_DATA+"correlations_v{0}_c{1}.csv".format(VERSION, iso_comp)
  else:
    fn = DIR_DATA+"correlations_v{version}.csv".format(version=VERSION)
  
  with open(fn, "w+") as file:
    writer = csv.writer(file)

    # header row
    writer.writerow(["author_name"] + keys)

    missing = 0
    def safe_get_attr_val(author_attrs, key):
      nonlocal missing
      # does have attribute
      if key in author_attrs:
        return author_attrs[key]
      # does not have attribute
      else:
        missing += 1
        return ""

    # entry rows
    for author_name, author_attrs in data.items():
      row = \
        ( [ author_name ]
        + [ safe_get_attr_val(author_attrs, key) for key in keys ] )
      writer.writerow(row)

    # print missing count
    print("missing attribute entries: {0}".format(missing))


