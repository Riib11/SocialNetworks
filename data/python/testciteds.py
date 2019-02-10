import json

file = open("citeds.json","r+")

string = ""
for line in file: string += line
jsonobj = json.loads(string)

print("loaded!")

file.close()
