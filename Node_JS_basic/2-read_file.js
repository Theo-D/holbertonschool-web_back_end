const fs = require('node:fs');

function countStudents(path) {
  let data = '';
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const dataArr = data.split('\n');
  const studentArr = dataArr.filter((elm) => elm !== dataArr[0] && elm !== '');
  const studentKeys = dataArr[0].split(',');

  const studentDict = studentArr.map((line) => {
    const object = line.split(',');
    return Object.fromEntries(
      studentKeys.map((key, index) => [key, object[index]])
    );
  });

  const byField = studentDict.reduce((accumulator, student) => {
    const { field } = student;
    const { firstname } = student;
    if (!accumulator[field]) {
      accumulator[field] = [];
    }
    accumulator[field].push(firstname);
    return accumulator;
  }, {});

  console.log(`Number of students: ${studentArr.length}`);

  for (const [key, value] of Object.entries(byField)) {
    console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
  }
}

module.exports = countStudents;
