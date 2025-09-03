function countStudents(path) {
  const fs = require('node:fs');

  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

    const dataArr = data.split('\n');
    const studentArr = dataArr.filter(elm => elm !== dataArr[0] && elm !== '');
    const studentKeys = dataArr[0].split(',');


    const studentDict = studentArr
    .map(line => {
      const object = line.split(',');
      return studentKeys.reduce((obj, h, i) => {
        obj[h] = object[i];
        return obj;
      }, {});
    });

    const byField = studentDict.reduce((accumulator, student) => {
      const field = student.field;
      const firstname = student.firstname;
      if(!accumulator[field]) {
        accumulator[field] = [];
      }
      accumulator[field].push(firstname);
      return accumulator;
    }, {});

    console.log(`Number of students: ${studentArr.length}`);

    for (const [key, value] of Object.entries(byField)) {
      console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
    }
  };

module.exports = countStudents;
