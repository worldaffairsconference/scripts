import random
import csv

# Takes input CSV that goes NAME | SCHOOL | PLEN 1 | PLEN 2 ...

# 1/2 Plenaries: AI and Sustainability
# 2/3 Plenaries: Bioinformatics and C150
# 1/3 Plenaries: Cyberwarfare and Tech in Developing

plen = ["China and the World", "Cryptocurrencies", "Drug Legalization", "Earth Overburdened", "Future of Feminism", "A Nuclear World"]

data = []
pick = [0,0,0,0,0,0]
count = [0,0,0,0,0,0]

def assign(n, plens):
    # dup assign is still a problem
    for i in range(4):
        number = random.randrange(0,len(n))
        if (plens[n[number]] == "True"):
            return n[number]
        else:
            n.pop(number)


with open('students.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in range(6):
            if (row[i+2] == "True"):
                pick[i] += 1
        data.append([row[0], row[1], [row[2],row[3],row[4],row[5],row[6],row[7]]])

with open('output-students.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Student Name", "Student School", "Plenary 1", "Plenary 2", "Plenary 3"])
    for row in data:
        final = [row[0],row[1]]
        # 1st Plen
        temp = assign([0,3,4,5],row[2])
        count[temp] += 1
        final.append(plen[temp])
        # 2nd Plen
        temp = assign([0,1,2,5],row[2])
        count[temp] += 1
        final.append(plen[temp])
        # 3rd Plen
        temp = assign([1,2,3,4],row[2])
        count[temp] += 1
        final.append(plen[temp])
        writer.writerow(final)
print pick
print count
