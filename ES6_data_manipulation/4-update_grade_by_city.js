export default function updateStudentGradeByCity (studentsArr, city, newGrades) {
  let newArr = Array();

  if (!Array.isArray(studentsArr)) {
    return newArr;
  }

  const gradeMap = new Map(newGrades.map(grade => [grade.studentId, grade.grade]));

  return studentsArr
  .filter(student => student.location === city)
  .map(student => ({
    id: student.id,
    firstName: student.name,
    location: student.location,
    grade: gradeMap.has(student.id) ? gradeMap.get(student.id) : 'N/A'
  }));
}
