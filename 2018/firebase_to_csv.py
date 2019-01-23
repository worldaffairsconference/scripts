import json
import csv

jsonFile = open("wac-registration-export.json",'r')
csvResults = open("students.csv",'w')

outputWriter = csv.writer(csvResults)

jsonData = json.load(jsonFile)

for user in jsonData['users'].values():
    if (user.get('students')):
        for students in user['students'].values():
            row = list(students.values())
            output = [row[1], row[0], row[4], row[5], row[6], row[7], row[8], row[9]]
            print output
            outputWriter.writerow(output)

jsonFile.close()
csvResults.close()
