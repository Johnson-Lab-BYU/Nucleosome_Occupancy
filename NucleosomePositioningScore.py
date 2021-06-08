import csv
import sys

positions = open(sys.argv[1])
dyads = open(sys.argv[2])
#positions file is a range.txt
#dyads file is dyas.csv
list = []
intlist = []
newlist = []
for line in positions:
    newlist = line[1:-1]
    list = newlist.split(', ')
for i in list:
    intlist.append(int(i))
#taking positions file to a list of intergers

adjustScore = int(sys.argv[3])
dyadsList = []
adjustedDyadsList = []
for line in dyads:
    dyadsList.append(int(line))
for i in dyadsList:
    adjustedDyadsList.append(i - adjustScore)

dyadScore = []
for i in intlist:
    range1 = range(i-150,i+150)
    range2 = range(i-10,i+10)
    x = 0
    y = 0
    for j in adjustedDyadsList:
        if j in range1:
            x += 1
        if j in range2:
            y += 1
    dyadScore.append(float(y)/float(x))

dyadDictionary = dict(zip(list,dyadScore))
name = str(sys.argv[4])+'_dyadDictionary.csv'
with open(name, 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dyadDictionary.items():
        writer.writerow([key,value])
