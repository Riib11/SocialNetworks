import json
import sys

if len(sys.argv)>1 and sys.argv[1].endswith(".json"):
	j = json.load(open(sys.argv[1],"r+"))
	print("[",len(j),"] items in",sys.argv[1])
else:
	print("need to provide one .json file")
