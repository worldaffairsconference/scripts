import random
import csv

# 1/2 Plenaries: AI and Sustainability
# 2/3 Plenaries: Bioinformatics and C150
# 1/3 Plenaries: Cyberwarfare and Tech in Developing

plen = ["Artificial Intelligence and the New World", "The New Age of Medicine: Bioinformatics", "Maintaining Canada's Global Presence", "The Future of Warfare", "Technology in the Developing World", "Roadmap to a Sustainable Future"]

data = []
pick = [0,0,0,0,0,0]
count = [0,0,0,0,0,0]

def assign(n, plens):
    for i in range(4):
        number = random.randrange(0,len(n))
        if (plens[n[number]] == "selected"):
            return n[number]
        else:
            n.pop(number)


with open('students.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in range(6):
            if (row[i+5] == "selected"):
                pick[i] += 1
        data.append([row[1],row[2],[row[5],row[6],row[7],row[8],row[9],row[10]],row[4]])

with open('output-students.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Student Name", "Student School", "Plenary 1", "Plenary 2", "Plenary 3", "Notes"])
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
        final.append(row[3])
        writer.writerow(final)
print pick
print count
