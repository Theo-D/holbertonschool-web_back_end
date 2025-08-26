export default function getStudentsByLocation (studentsArr, city) {
  const newArr = Array();

  if (!Array.isArray(studentsArr)) {
    return newArr;
  }

  newArr = studentsArr.filter(student => student.location === city);

  return newArr;
}
