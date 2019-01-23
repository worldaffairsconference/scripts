def readCSVSpecial(filename):
    f = open(filename + ".csv", "r")
    lst = f.read().split("\n")
    for i in range(len(lst)):
        lst[i] = lst[i].split(",")
        for k in range(len(lst[i])):
            lst[i][k] = str(lst[i][k])[1:len(lst[i][k])-1]
    return lst

def readCSV(filename):
    f = open(filename + ".csv", "r")
    lst = f.read().split("\n")
    for i in range(len(lst)):
        lst[i] = lst[i].split(",")
    return lst

def writeCSV(filename, permissions, lst):
    s = ""
    f = open(filename + ".csv", permissions)
    for i in lst:
        for k in i:
            s += str(k) + ","
        s = s[0:len(s)-1]
        s+="\n"
        f.write(s)
        s = ""
