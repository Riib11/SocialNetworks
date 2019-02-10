import json, sys

try:

    o = json.load(open(sys.argv[1], "r+"))
    print("success!")
    print("len =",len(o))

except Exception as e:

    print("failure :(")
    raise e
