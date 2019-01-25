import json
import csv

jsonFile = open("Data/wac-registration-export.json",'r')
csvResults = open("Data/FBstudents.csv",'w')

outputWriter = csv.writer(csvResults)

data = json.load(jsonFile)

for user in data["users"].values(): #For all accounts
    if user.get("students"): #Check if the person actually has students
        for student in user["students"].values():
            try: #Sometimes data was messed up with missing values so this checks for the errors and shows us the invalid data
                #JSON parser was reading in random order so we are just getting the specific values
                n = student["name"]
                a = student["accessibility"]
                if a == "": a = "None"
                p1 = student["panel1"]
                p2 = student["panel2"]
                p3 = student["panel3"]
                p4 = student["panel4"]
                p5 = student["panel5"]
                p6 = student["panel6"]
                row = [n, a, p1, p2, p3, p4, p5, p6]
                print(row)
                outputWriter.writerow(row)
            except: #Error in data
                outputWriter.writerow("ERROR")
                #ANSI Escape Sequence
                # \033[95m is the escape sequence for a bright pink colour
                # \033[0m is an escape sequence that ends colour formatting (otherwise will continue in rest of output
                print("\033[95m" + "ERROR" + "\033[0m")
                print(list(student.values()))

jsonFile.close()
csvResults.close()
