import random
import csv

#Plenaries
"""
Data Daycare
Popular Defiance
Reconciliation and Indigenization
Startup Cleanup
The EU’s Midlife Crisis
The Plight of Workers’ Rights
"""

plen = ["Data Daycare", "Popular Defiance", "Reconciliation and Indigenization", "Startup Cleanup", "The EU’s Midlife Crisis", "The Plight of Workers’ Rights"]

data = []
school = "Upper Canada College"

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

# This just imports the CSV and does some counting on plenary information.
with open('Data/gsheets-students.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        final = [row[2], school]
        preflist = [row[3],row[4],row[5],row[6]]
        if (allUnique(preflist) == False):
            temp = ["True","True","True","True","False","False"]
            random.shuffle(temp)
            final = final + temp
        else:
            for i in range(6):
                if plen[i] in preflist:
                    final.append("True")
                else:
                    final.append("False")
        data.append(final)

data.pop(0)

with open('Data/formatted-students.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        print(row)
        writer.writerow(row)
