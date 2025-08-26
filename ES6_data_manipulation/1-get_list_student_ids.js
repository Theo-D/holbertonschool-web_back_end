export default function getListStudentIds (studentsArr) {

  if (!Array.isArray(studentsArr)) {
    return [];
  }

  return studentsArr.map(student => student.id);
}
