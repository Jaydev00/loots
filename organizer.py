import os
import json
from datetime import datetime
from pprint import pprint

REMOVE_LEAGUES = True

files = os.listdir()
leaguesIVStart = int(datetime(2023,11,15,0,0,0).timestamp())
leaguesIVEnd = int(datetime(2024,1,7,0,0,0).timestamp())
#print(f"leaguesIVStart {leaguesIVStart}, leaguesIVEnd {leaguesIVEnd}")

try:
    os.mkdir('sorted')
except Exception:
    pass
pprint(files)

for file in files:
    if '.py' in file or not os.path.isfile(file):
        continue
    print(file)
    f = open(file, "r")
    entries = f.read().split('\n')
    entries.pop()
    entries.sort(key=lambda x: int(datetime.strptime(json.loads(x)["date"], '%b %d, %Y, %I:%M:%S %p').timestamp()))
    entriesToRemove = []
    for entry in entries:
        if not len(entry) > 0:
            continue
        dateStamp = json.loads(entry)["date"]
        epochSeconds = int(datetime.strptime(dateStamp, '%b %d, %Y, %I:%M:%S %p').timestamp())
        if epochSeconds > leaguesIVStart and epochSeconds < leaguesIVEnd:
            print(f"{dateStamp} during leagues IV")
            if(REMOVE_LEAGUES):
                entriesToRemove.append(entry)
            continue
        #print("%d: Date Stamp: %s, Epoch: %d"%(i, dateStamp, int(datetime.strptime(json.loads(entry)["date"],'%b %d, %Y, %I:%M:%S %p').strftime('%s'))))
    for entry in entriesToRemove:
        entries.remove(entry)
    i = 1
    while i < len(entries):
        if len(entries[i]) > 0:
            jsonstring = entries[i]
            jsonstring2 = entries[i-1]
            dateStamp = json.loads(entries[i])["date"]
            if json.loads(jsonstring)["date"] == json.loads(jsonstring2)["date"] and (json.loads(jsonstring)["drops"] == json.loads(jsonstring2)["drops"]):
                print("In file %s, %d: duplicate: %s, drops: '%s'"%(file, i, dateStamp, json.loads(jsonstring)["drops"]))
                #entries.remove(jsonstring)
            if json.loads(jsonstring)["drops"] == []:
                print("In file %s, %d: empty drops: %s, drops: %s"%(file, i, dateStamp, json.loads(jsonstring)["drops"]))
        i+=1
    w = open('sorted/%s'%file, "w")
    w.write("\n".join(entries))
    w.write("\n")