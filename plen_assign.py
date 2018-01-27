import random
import csv

# Takes input CSV that goes NAME | SCHOOL | PLEN 1 | PLEN 2 ...
# For each plen, values are strings - "True" or "False", though those are easily changeable

# 1/2 Plenaries: China and Drugs
# 2/3 Plenaries: Feminism
# SPECIAL CASE: 2: Cryptocurrencies
# 1/3 Plenaries: Earth and Nuclear

# Therefore,
# Session 1: China (0), Drugs (2), Earth (3), Nuclear (5)
# Session 2: China (0), Cryptocurrencies(1) Drugs (2), Feminism (4)
# Session 3: Earth (3), Feminism (4), Nuclear (5)


plen = ["China and Africa's New Era", "Cryptocurrencies: Friend or Foe?", "Drug Legalization in a Progressive World", "The Global Food Crisis", "The Changing Face of Feminism", "Nuclear Weapons: Obsolete or the Future?"] # the plenaries, in ALPHABETICAL order (super super important)

# these arrays get populated in the future
data = []
pick = [0,0,0,0,0,0]
count = [0,0,0,0,0,0]

def assign(n, plens):
    # n is the plenaries available for the timeslot, plens is the preferences they chose
    # this just does one-time assignment: assigns a random plen, and checks if it's possible within that timeslot
    # if none of them are available (which is only a problem if one of the sessions doesn't run twice), then they get a random one (sorry)
    og = len(n) # placeholder as a "just in case"
    for i in range(len(plens)):
        if (len(n) != 0):
            number = random.randrange(0,len(n))
            if (plens[n[number]] == "True"):
                return n[number]
            else:
                n.pop(number)
        else:
            return random.randrange(0,og)

# This just imports the CSV and does some counting on plenary information.
with open('students.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in range(6):
            if (row[i+2] == "True"):
                pick[i] += 1
        data.append([row[0], row[1], [row[2],row[3],row[4],row[5],row[6],row[7]]])

# This does the meat of script, doing some calculations and writing to the output CSV.
with open('output-students.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Student Name", "Student School", "Plenary 1", "Plenary 2", "Plenary 3"])
    for row in data: # this is the loop that handles each student
        final = [row[0],row[1]] # student name and school need no manipulation

        # this next bit can be confusing, since it's not coded well
        # for each session, we use the assign() function to assign a random plenary to the delegate
        # temp is the index in plen[] that corresponds to each plenary
        # then, we upp the counter, add it to the "write" array, and set that plenary preference to false - which is a hack solution, but it's the best way to handle duplicates without rewriting everything (which it should)

        # 1st Session
        temp = assign([0,2,3,5],row[2])
        count[temp] += 1
        final.append(plen[temp])
        row[2][temp] = "False"

        # 2nd Session
        temp = assign([0,1,2,4],row[2])
        count[temp] += 1
        final.append(plen[temp])
        row[2][temp] = "False"

        # 3rd Session
        temp = assign([3,4,5],row[2])
        count[temp] += 1
        final.append(plen[temp])
        row[2][temp] = "False"
        print final
        writer.writerow(final)
print "Plenary prefrences: "
print pick
print "Plenary assignments: "
print count
