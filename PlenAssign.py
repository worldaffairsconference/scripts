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

Laidlaw (650) - Startup Cleanup
Gym (100) - The EU’s Midlife Crisis
Theater (100) - Data Daycare
Library (80) - Popular Defiance
RM 123 (75) - The Plight of Workers’ Rights
RM 138 (75) - Reconciliation and Indigenization
"""

data = []
pick = [0,0,0,0,0,0]
count = [0,0,0,0,0,0]

countSemi = [[0,-1,0,-1,0,0],[-1,0,0,0,0,-1],[0,0,-1,0,-1,0]]

#Room capacities
rmLaidlaw = 650 #650
rmGym = 100 #100
rmLecture = 100 #100
rmLibrary = 80 #80
rm124 = 75 #75
rm138 = 75 #75
#Data, Defiance, Reconcil, Startup, EU, Rights
newCap = [[rmLecture, -1, rm138, -1, rmLaidlaw, rmLecture], [-1, rmLecture, rm138, rmLaidlaw, rmGym, -1], [rmLecture, rmLaidlaw, -1, rm138, -1, rmGym]]

def assign(n, plens, id):
    #n is the plenaries in the given timeslot
    #plens is the plens that they want to join
    #id is the plen number
    #randomly assigns plenaries hopefully within their chosen (if they are full or none are available if one did not run twice they get a random plenary)
    og = len(n)#max number of plenaries in the start
    _n = n.copy()
    for i in range(len(plens)):
        if len(n) != 0:
            number = random.randrange(0, len(n))
            if plens[n[number]] == "True" and countSemi[id][n[number]] < newCap[id][n[number]]:
                return n[number]
            else:
                n.pop(number)
        else:
            checker = list(range(0, og))
            random.shuffle(checker)
            try:
                while plens[_n[checker[0]]] == "FalseFalse" or countSemi[id][_n[checker[0]]] >= newCap[id][_n[checker[0]]]:
                    checker.pop(0)
            except:
                print("Not enough spaces. Uh oh")
                exit(1)
            return _n[checker[0]]

#read CSV and count of choices and format list
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

        #basically we run the assign function and store in in temp so we know which plenary they will attend for the timeslot
        #afterwards we change a couple of counts and get the output structured
        #we run it 3 times as we have 3 sessions

        #True - Want to go
        #False - Don't want to go (but who cares)
        #FalseFalse - Already have gone

        plenChoices = row[2]
        print(row[0])

        #1st Session
        temp = assign([0, 2, 4, 5], plenChoices, 0)
        count[temp] += 1
        countSemi[0][temp] += 1
        final.append(plen[temp])
        row[2][temp] = "FalseFalse"

        #2nd Session
        temp = assign([1, 2, 3, 4], plenChoices, 1)
        count[temp] += 1
        countSemi[1][temp] += 1
        final.append(plen[temp])
        row[2][temp] = "FalseFalse"

        #3rd Session
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
print(countSemi)