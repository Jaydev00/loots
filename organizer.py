import os
import json
from datetime import datetime

files = os.listdir()
#os.mkdir('sorted')
for file in files:
    if '.py' in file or not os.path.isfile(file):
        continue
    f = open(file, "r")
entries = f.read().split('\n')
i = 0
entries.pop()
entries.sort(key=lambda x: int(datetime.strptime(json.loads(x)["date"],'%b %d, %Y, %I:%M:%S %p').strftime('%s')), reverse=True)
for entry in entries:
    if not len(entry) > 0:
        continue
    dateStamp = json.loads(entry)["date"]
    #print("%d: Date Stamp: %s, Epoch: %d"%(i, dateStamp, int(datetime.strptime(json.loads(entry)["date"],'%b %d, %Y, %I:%M:%S %p').strftime('%s'))))
    i+=1
i = 1
while i < len(entries):
    if len(entries[i]) > 0:
        jsonstring = entries[i]
        jsonstring2 = entries[i-1]
        dateStamp = json.loads(entries[i])["date"]
        if json.loads(jsonstring)["date"] == json.loads(jsonstring2)["date"] and (json.loads(jsonstring)["drops"] == json.loads(jsonstring2)["drops"]):
            print("%d: Removing duplicate: %s, drops: %s"%(i, dateStamp, json.loads(jsonstring)["drops"]))
            entries.remove(jsonstring)
    i+=1
w = open('sorted/%s'%file, "w")
w.write("\n".join(entries))
w.write("\n")