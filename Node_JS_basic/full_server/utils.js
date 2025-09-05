import fs from 'node:fs';

export default function readDatabase(dbPath) {
  return new Promise((resolve, reject) => {
    fs.readFile(dbPath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const dataArr = data.split('\n');
      const header = dataArr[0];
      const studentKeys = header.split(',');
      const studentArr = dataArr.slice(1).filter((line) => line.trim() !== '');

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

      const orderedFields = Object.keys(byField)
        .sort()
        .reduce((acc, key) => ({ ...acc, [key]: byField[key] }), {});

      resolve(orderedFields);
    });
  });
}
