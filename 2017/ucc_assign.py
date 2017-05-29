import random
import csv

# 1/2 Plenaries: AI and Sustainability
# 2/3 Plenaries: Bioinformatics and C150
# 1/3 Plenaries: Cyberwarfare and Tech in Developing

plen = ["Artificial Intelligence and the New World", "The New Age of Medicine: Bioinformatics", "Maintaining Canada's Global Presence", "The Future of Warfare", "Technology in the Developing World", "Roadmap to a Sustainable Future"]
data = []
pick = [0,0,0,0,0,0]
count = [0,0,0,0,0,0]

def convert(pinput):
    tempcount = 0
    response = ["unselected","unselected","unselected","unselected","unselected","unselected"]
    for i in range(6):
        for j in range(4):
            print pinput[j]
            if (pinput[j] == plen[i] and response[i] == "unselected"):
                response[i] = "selected"
                pick[i] += 1
                tempcount += 1
    if (tempcount < 4):
        return ["unselected", "unselected", "selected", "selected", "selected", "selected"]
    return response

def assign(n, plens):
    for i in range(4):
        number = random.randrange(0,len(n))
        if (plens[n[number]] == "selected"):
            return n[number]
        else:
            n.pop(number)

with open('ucc-students.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    skipped = False
    for row in csvreader:
        if (skipped == False):
            skipped = True
        else:
            data.append([row[2],[row[3],row[4],row[5],row[6]]])

with open('output-ucc-students.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Student Name", "Student School", "Plenary 1", "Plenary 2", "Plenary 3", "Notes"])
    for row in data:
        print row
        final = [row[0], "Upper Canada College"]
        sorted = convert(row[1])
        # 1st Plen
        temp = assign([0,3,4,5],sorted)
        count[temp] += 1
        final.append(plen[temp])
        # 2nd Plen
        temp = assign([0,1,2,5],sorted)
        count[temp] += 1
        final.append(plen[temp])
        # 3rd Plen
        temp = assign([1,2,3,4],sorted)
        count[temp] += 1
        final.append(plen[temp])
        final.append("N/A")
        writer.writerow(final)
print pick
print count
