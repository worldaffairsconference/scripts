#Light script to change the Google Spreadsheet Registration into a Compressed CSV with formatting cleaned up
import CsvParsing as cp
lst = cp.readCSVSpecial("WAC Plenaries 2019: UCC")
_lst = [["Username", "EU", "Data", "Reconciliation", "Startup", "Rights", "Defiance", "Dietary Restrictions"]]
print(_lst[0])

_eu = 0
_data = 0
_reconciliation = 0
_startup = 0
_rights = 0
_defiance = 0

for i in range(1, len(lst)):
    eu = lst[i].count("The EU’s Midlife Crisis")>=1
    data = lst[i].count("Data Daycare")>=1
    reconciliation = lst[i].count("Reconciliation and Indigenization")>=1
    startup = lst[i].count("Startup Cleanup")>=1
    rights = lst[i].count("The Plight of Workers’ Rights")>=1
    defiance = lst[i].count("Popular Defiance")>=1

    #Count section
    _eu+=int(eu)
    _data+=int(data)
    _reconciliation+=int(reconciliation)
    _startup+=int(startup)
    _rights+=int(rights)
    _defiance+=int(defiance)

    _lst.append([lst[i][1], eu, data, reconciliation, startup, rights, defiance, lst[i][6]])
cp.writeCSV("2019Comp", "w", _lst)

#Print Count Section
print("EU: " + str(_eu))
print("Data: " + str(_data))
print("Reconciliation: " + str(_reconciliation))
print("Starup: " + str(_startup))
print("Rights: " + str(_rights))
print("Defiance: " + str(_defiance))