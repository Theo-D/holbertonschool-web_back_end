module.exports = async function countStudents (path) {
  const fs = require('node:fs/promises');

  try {
    const data = await fs.readFile(path, {encoding: 'utf8'});

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

    let output = `Number of students: ${studentArr.length}`;
    for (const [key, value] of Object.entries(byField)) {
      output += `\nNumber of students in ${key}: ${value.length}. List: ${value.join(', ')}`;
    }

    console.log(output);

    return output;
  }
  catch (err) {
    console.error('Error: Cannot load the database');
    console.error(err);
  }
}
