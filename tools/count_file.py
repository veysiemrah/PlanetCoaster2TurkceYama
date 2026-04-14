import json, sys
data = json.loads(open(sys.argv[1], encoding="utf-8").read())
print(len(data))
