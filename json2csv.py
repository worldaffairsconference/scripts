import json
import csv

jsonFile = open("wac-registration-export.json",'r')
csvResults = open("wac-registraction.csv",'w')

outputWriter = csv.writer(csvResults)

jsonData = json.load(jsonFile)

for user in jsonData['users'].values():
  if (user.get('students')):
    for students in user['students'].values():
      outputWriter.writerow(list(students.values()))

jsonFile.close()
csvResults.close()