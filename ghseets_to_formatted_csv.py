import random
import csv

# The Feminism plen name was changed because of an error in the gsheet

plen = ["China and Africa's New Era", "Cryptocurrencies: Friend or Foe?", "Drug Legalization in a Progressive World", "The Global Food Crisis", "The Future of Feminism", "Nuclear Weapons: Obsolete or the Future?"]

data = []
school = "Upper Canada College"

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

# This just imports the CSV and does some counting on plenary information.
with open('gsheets-students.csv', 'rb') as csvfile:
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

with open('formatted-students.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        print row
        writer.writerow(row)
