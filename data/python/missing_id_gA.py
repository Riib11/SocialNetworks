import json

# abbreviation: mid ::= missing id

with open("../gA.json", "r+") as file: gA_list = json.load(file)

mid_gA_list = [ p for p in gA_list if not "id" in p ]

print(len(mid_gA_list))
