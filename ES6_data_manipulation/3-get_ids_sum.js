export default function getStudentIdsSum (studentsArr) {
  let newArr = Array();

  if (!Array.isArray(studentsArr)) {
    return newArr;
  }

  let idSum = 0;

idSum = studentsArr.reduce((accumulator, currentValue) => {
  return accumulator + currentValue.id;
  },
  idSum);

  return idSum;
}
