import random
import csv

#1/2: EU, Reconcil
#2/3: Startup, Defiance
#1/3: Data, Rights

#S1: Data(0), Reconcil(2), EU(4), Rights(5)
#S2: Defiance(1), Reconcil(2), Startup(3), EU(4)
#S3: Data(0), Defiance(1), Startup(3), Rights(5)

plen = ["Data Daycare", "Popular Defiance", "Reconciliation and Indigenization", "Startup Cleanup", "The EU’s Midlife Crisis", "The Plight of Workers’ Rights"]

""" Ideal Locations
Place (capacity) - Ideal Plenary

Laidlaw (500ish) - Startup Cleanup
Gym (100ish) - The EU’s Midlife Crisis
Theater (80ish) - Data Daycare
Library (80ish) - Popular Defiance
RM 123 (60ish) - The Plight of Workers’ Rights
RM 138 (60ish) - Reconciliation and Indigenization
"""

data = []
pick = [0,0,0,0,0,0]
count = [0,0,0,0,0,0]

countSemi = [[0,-1,0,-1,0,0],[-1,0,0,0,0,-1],[0,0,-1,0,-1,0]]

#Room capacities
rmLaidlaw = 500 #500
rmGym = 100 #100
rmTheater = 80 #80
rmLibrary = 80 #80
rm123 = 60 #60
rm138 = 60 #60
#      80         80         60       500        100    60
#      Data       Defiance   Reconcil Startup    EU     Rights
cap = [rmTheater, rmLibrary, rm138,   rmLaidlaw, rmGym, rm123] #Never should change this

broken = 0

def assign(n, plens, id):
    #n is the plenaries in the given timeslot
    #plens is the plens that they want to join
    #id is the plen number
    #Randomly assigns plenaries hopefully within their chosen (if they are full or none are available if one did not run twice they get a random plenary)
    og = len(n) #Max number of plenaries in the start
    _n = n.copy()
    for i in range(len(plens)):
        if len(n) != 0:
            number = random.randrange(0, len(n))
            if plens[n[number]] == "True" and countSemi[id][n[number]] < cap[n[number]]:
                return n[number]
            else:
                n.pop(number)
        else:
            checker = random.randrange(0, og)
            while plens[_n[checker]] == "FalseFalse" or countSemi[id][_n[checker]] >= cap[_n[checker]]:
                    #global broken
                    #broken += 1
                checker = random.randrange(0, og)
            return _n[checker]

#Read CSV and count of choices and format list
with open("Data/students.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in range(6):
            if (row[i+2] == "True"):
                pick[i] += 1
        data.append([row[0], row[1], [row[2],row[3],row[4],row[5],row[6],row[7]]])

with open("Data/plenaryAssign.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Student Name", "Plenary 1", "Plenary 2", "Plenary 3"])
    for row in data: # this is the loop that handles each student
        final = [row[0]]

        # this next bit can be confusing, since it's not coded well
        # for each session, we use the assign() function to assign a random plenary to the delegate
        # temp is the index in plen[] that corresponds to each plenary
        # then, we upp the counter, add it to the "write" array, and set that plenary preference to false - which is a hack solution, but it's the best way to handle duplicates without rewriting everything (which it should)

        plenChoices = row[2]
        print(row[0])

        # 1st Session
        #print(row[0])
        #print("Assign 1")
        temp = assign([0, 2, 4, 5], plenChoices, 0)
        count[temp] += 1
        countSemi[0][temp] += 1
        final.append(plen[temp])
        row[2][temp] = "FalseFalse"
        #True - Want to go
        #False - Don't want to go
        #FalseFalse - Already have gone

        # 2nd Session
        #print("Assign 2")
        temp = assign([1, 2, 3, 4], plenChoices, 1)
        count[temp] += 1
        countSemi[1][temp] += 1
        final.append(plen[temp])
        row[2][temp] = "FalseFalse"

        # 3rd Session
        #print("Assign 3")
        temp = assign([0, 1, 3, 5], plenChoices, 2)
        count[temp] += 1
        countSemi[2][temp] += 1
        final.append(plen[temp])
        row[2][temp] = "FalseFalse"

        print(final)
        print(count)
        print(countSemi)
        writer.writerow(final)
print("Plenary prefrences: ")
print(pick)
print("Plenary assignments: ")
print(count)
print(broken)
print(countSemi)