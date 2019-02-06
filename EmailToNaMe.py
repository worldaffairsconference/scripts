import csv

final = []

"""
When the code crashes that means that it is done reading the UCC emails as it tries to capitalize a non list
This is shit coding but just a quick fix
"""

with open("Data/plenaryAssign.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for person in csvreader:
        try:
            if person[0] != "Student Name":
                nAmE = person[0].split("@")
                nAmE = nAmE[0].split(".")
                _nAmE = ""
                nAmE[0] = nAmE[0].capitalize()
                _nAmE += nAmE[0] + " "
                nAmE[1] = nAmE[1].capitalize()
                _nAmE += nAmE[1] + " "
                try: #Sometimes people have name1.name2.name3@ucc.on.ca for some reason ;(
                    nAmE[2] = nAmE[2].capitalize()
                    _nAmE += nAmE[2]
                except: #Literally going to trigger 99.99% of the time
                    pass
                final.append([_nAmE, person[1], person[2], person[3]])
            else:
                final.append(person)
        except:
            pass #who cares just read comment at top
with open("Data/plenaryAssignNaMe.csv", "w") as c:
    writer = csv.writer(c)
    for p in final:
        writer.writerow(p)