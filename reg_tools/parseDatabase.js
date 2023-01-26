// Depends on reg_tools/export.json (Firebase Console > Realtime Database > Export JSON)

const fs = require("fs");
const file = fs.readFileSync("./export.json")
const data = JSON.parse(file);

console.log(`🏁 Loaded ${Buffer.byteLength(file)} bytes from export.json`);

let students = [];
let teachers = [];

const teachersKeys = Object.keys(data.teachers);

for (let i = 0; i < teachersKeys.length; i++) {
  // Loop through teachers
  let teacher = data.teachers[teachersKeys[i]];
  teachers.push({
    name: teacher.name,
    email: teacher.email,
    school: teacher.school,
    phone: teacher.phone,
  });

  if (!teacher.students) {
    continue; // No students
  }

  const studentKeys = Object.keys(teacher.students);

  for (let j = 0; j < studentKeys.length; j++) {
    // Loop through students
    let student = teacher.students[studentKeys[j]];
    students.push({
      name: student.name,
      email: student.email,
      school: teacher.school,
      grade: student.grade,
      plen1: student.p1 || "Not selected",
      plen2: student.p2 || "Not selected",
      plen3: student.p3 || "Not selected",
    });
  }
}

console.log(
  `🏁 Read ${teachers.length} teachers and ${students.length} students totalling ${teachers.length + students.length} records.`
);

// Write to CSV
fs.writeFileSync(
  "./users.csv",
  "name,email,phone,school,grade,plen1,plen2,plen3\n"
);
for (let i = 0; i < students.length; i++) {
  let student = students[i];
  fs.appendFileSync(
    "./users.csv",
    `${student.name},${student.email},"n/a",${student.school},${student.grade},${student.plen1},${student.plen2},${student.plen3}\n`
  );
}
for (let i = 0; i < teachers.length; i++) {
  let teacher = teachers[i];
  fs.appendFileSync(
    "./users.csv",
    `${teacher.name},${teacher.email},${teacher.phone},${teacher.school},"n/a","n/a","n/a","n/a"\n`
  );
}

plenArr[i]["students"].includes(uid)