export default function getListStudentIds (studentsArr) {
  const newArr = Array();

  if (!Array.isArray(studentsArr)) {
    return newArr;
  }

  newArr = studentsArr.map(student => student.id);

  return newArr;
}
