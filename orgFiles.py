import os
import re
import datetime
import dateparser

data = dict()
leagues3Start = datetime.datetime(2022,1,19,0,0,0)
leagues3End = datetime.datetime(2022,3,16,23,59,59)

def sortFunc(x):
    return x[1]

cwdlogs = os.getcwd() + "/logs"
cwdOutput = os.getcwd() + "/output"
for inputFile in os.listdir(cwdlogs):
    infile = open(cwdlogs + "/" + inputFile, "r")

    for x in infile:
        monster = re.search("\"name\":\"(.+)\",\"level\"", x).group(1)
        date = dateparser.parse(re.search("\"date\":\"(.+)\"", x).group(1))
        entry = [monster, date, x]
        if date > leagues3Start and date < leagues3End:
            continue
        if not (monster in data.keys()):
            data.update({monster:list(list())})
        data.get(monster).append(entry)
for category in data.keys():
    data.update({category:sorted(data[category], key=sortFunc)})

for category in data.keys():
    print(category)
    ofile = open(cwdOutput + "/" + category + ".log", "a")
    for entry in data[category]:
        ofile.write(entry[2])
        #print(entry[1].strftime("%m/%d/%Y, %H:%M:%S") + " " + entry[2], end ='')
    #outputFile = open("output.log", "a")
    #for y in entries:
    #    outputFile.write(y[2])




