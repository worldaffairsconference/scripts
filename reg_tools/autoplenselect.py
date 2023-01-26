import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# initialize firebase
cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://worldaffairscon-8fdc5-default-rtdb.firebaseio.com"})

plenaries = db.reference('plenaries').get();
plenArr = []
plenArrInitial = []
uniqueStudents = []

# Loop through object plenaries
for key, value in plenaries.items():
    if (key == "open"):
      continue;
    # Append the plenary to the plenary array
    plenArr.append({
      "id": key,
      "maximum": value['max'],
      "current": len(value['students']),
      "students": value['students']
    });
    plenArrInitial.append({
      "id": key,
      "maximum": value['max'],
      "current": len(value['students']),
      "students": value['students']
    });

print("🏁 Fetched and parsed initial plenary data:")

def recomputePercentages():
  # Loop through plenary array
  for plenary in plenArr:
    # Compute the percentage of the plenary
    plenary['percentage'] = plenary['current'] / plenary['maximum'];

recomputePercentages();

moves = [];

def setStudent(uid, plenKey, teacherKey):
  # Get lowest percentage plenary
  lowest = plenArr[0];
  index = 0;

  for i in range(len(plenArr)):
    if (plenArr[i]['percentage'] < lowest['percentage']):
      if (not uid in plenArr[i]['students']):
        lowest = plenArr[i];
        index = i;

  if (not uid in uniqueStudents):
    uniqueStudents.append(uid);

  plenArr[index]['students'][uid] = True;
  moves.append({
    "target": "uidToPlen",
    "uid": uid,
    "plenTarget": plenArr[index]["id"],
  })

  lowest['current'] += 1;
  recomputePercentages();
  moves.append({
    "target": "plenToUid",
    "uid": uid,
    "plenKey": plenKey,
    "plenTarget": lowest["id"],
    "teacherKey": teacherKey
  });


teachers = db.reference('teachers').get();
for key, value in teachers.items():
  # Loop through students
  if (not "students" in value):
    continue;
  students = value['students'];
  for studentKey, studentValue in students.items():
    if not studentValue["p1"] or (studentValue["p1"] == ""):
      setStudent(studentKey, "p1", key);
    if not studentValue["p2"] or (studentValue["p2"] == ""):
      setStudent(studentKey, "p2", key);
    if (not "p3" in studentValue):
      setStudent(studentKey, "p3", key);
      continue;
    elif not studentValue["p3"] or (studentValue["p3"] == ""):
      setStudent(studentKey, "p3", key);

for i in range(len(plenArr)):
  print("🏁 Planned " + str(plenArr[i]['current'] - plenArrInitial[i]['current']) + " students to " + plenArr[i]['id'] + " (" + str(plenArrInitial[i]['current']) + "/" + str(plenArrInitial[i]['maximum']) + " to " + str(plenArr[i]['current']) + "/" + str(plenArr[i]['maximum']) + ")");

print("🏁 Performing " + str(len(moves)) + " moves across " + str(len(uniqueStudents)) + " unique students.");

for move in moves:
  if (move['target'] == "uidToPlen"):
    # db.reference('plenaries/' + move['plenTarget'] + '/students/' + move['uid']).set(True);
    print("🔥 Moved " + move['uid'] + " to " + move['plenTarget'] + " at plenary document.");
  elif (move['target'] == "plenToUid"):
    # db.reference('teachers/' + move['teacherKey'] + '/students/' + move['uid'] + "/" + move['plenKey']).set(move['plenTarget']);
    print("🔥 Set " + move['uid'] + " to " + move['plenTarget'] + " at position " + move["plenKey"] + " at student document.");

# print("✅ All done!");