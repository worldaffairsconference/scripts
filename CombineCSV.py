import csv

def reorder(lst): #Reorders the list as it was in the wrong order ;(
    kst = []
    kst.append(lst[0])
    kst.append(lst[1])
    kst.append(lst[4])
    kst.append(lst[7])
    kst.append(lst[6])
    kst.append(lst[3])
    kst.append(lst[2])
    kst.append(lst[5])
    return(kst)

with open("Data/students.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    with open("Data/GSstudents.csv", "r") as csvfile:
        GScsvreader = csv.reader(csvfile)
        for row in GScsvreader:
            writer.writerow(reorder(row))
    with open("Data/FBStudents.csv", "r") as csvfile:
        FBcsvreader = csv.reader(csvfile)
        for row in FBcsvreader:
            writer.writerow(reorder(row))