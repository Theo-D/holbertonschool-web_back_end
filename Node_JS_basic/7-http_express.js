const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = process.env.PORT || 1245;
const db = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  console.log(db);
  countStudents(db)
    .then((data) => res.send(`This is the list of our students\n${data}`))
    .catch((err) => res.send(`This is the list of our students\n${err.message}`));
});

app.listen(port, () => {
  console.log(`Server app listening on port ${port}`);
});

module.exports = app;
