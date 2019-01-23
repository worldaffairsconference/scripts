import json
import csv

jsonFile = open("Data/wac-registration-export.json",'r')
csvResults = open("Data/students.csv",'w')

outputWriter = csv.writer(csvResults)

jsonData = json.load(jsonFile)

for user in jsonData['users'].values():
    if (user.get('students')):
        for students in user['students'].values():
            row = list(students.values())
            print(row)
            r1 = row[1]
            r0 = row[0]
            r4 = row[4]
            r5 = row[5]
            r6 = row[6]
            r7 = row[7]
            r8 = row[8]
            r9 = row[9]
            output = [row[1], row[0], row[4], row[5], row[6], row[7], row[8], row[9]]
            print(output)
            outputWriter.writerow(output)

jsonFile.close()
csvResults.close()
