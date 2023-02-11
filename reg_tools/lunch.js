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
      teachername: teacher.name,
      teacheremail: teacher.email,
      grade: student.grade,
      uid: studentKeys[j],
      plen1: student.p1 || "Not selected",
      plen2: student.p2 || "Not selected",
      plen3: student.p3 || "Not selected",
    });
  }
}

console.log(
  `🏁 Read ${teachers.length} teachers and ${students.length} students totalling ${teachers.length + students.length} records.`
);


// Get lunch status for each student
for (let i = 0; i < students.length; i++) {
  if (data.lunch[students[i].uid] && data.lunch[students[i].uid].name) {
    students[i].lunch = true;
    students[i].uccid = data.lunch[students[i].uid].uccid;
  }
  else {
    students[i].lunch = false;
    students[i].uccid = "n/a";
  }
}


// Organize by school
let schools = {};
for (let i = 0; i < students.length; i++) {
  let student = students[i];
  if (!schools[student.school]) {
    schools[student.school] = [];
  }
  schools[student.school].push(student);
}

// Write name, lunch status, ucc id to per-school CSV
for (let school in schools) {
  fs.writeFileSync("./" + school + ".csv", "name,lunch,uccid,teachername,teacheremail\n");
  for (let i = 0; i < schools[school].length; i++) {
    fs.appendFileSync(
      "./" + school + ".csv",
      `${schools[school][i].name},${schools[school][i].lunch},${schools[school][i].uccid},${schools[school][i].teachername},${schools[school][i].teacheremail},\n`
    );
  }
}
