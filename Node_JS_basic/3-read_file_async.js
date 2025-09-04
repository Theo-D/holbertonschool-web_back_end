const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const dataArr = data.split('\n');
      const header = dataArr[0];
      const studentArr = dataArr.slice(1).filter((line) => line.trim() !== '');

      const studentKeys = header.split(',');

      const studentDict = studentArr.map((line) => {
        const values = line.split(',');
        return Object.fromEntries(
          studentKeys.map((key, index) => [key.trim(), values[index].trim()]),
        );
      });

      const byField = studentDict.reduce((acc, student) => {
        const { field, firstname } = student;
        if (!acc[field]) {
          acc[field] = [];
        }
        acc[field].push(firstname);
        return acc;
      }, {});

      let output = `Number of students: ${studentArr.length}`;
      console.log(`Number of students: ${studentArr.length}`);

      for (const [field, names] of Object.entries(byField)) {
        const line = `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        output += `\n${line}`;
        console.log(line);
      }
      resolve(output);
    });
  });
}

module.exports = countStudents;
