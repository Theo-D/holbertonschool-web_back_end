const { createServer } = require('node:http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;
const db = process.argv[2];

const app = createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/' && req.method === 'GET') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students' && req.method === 'GET') {
    countStudents(db)
      .then((output) => {
        res.statusCode = 200;
        res.end(`This is the list of our students\n${output}`);
      })
      .catch(() => {
        res.statusCode = 404;
        res.end('Cannot load the database');
      });
    return;
  }

  res.statusCode = 404;
  res.end('Not Found');
});

app.listen(port, hostname);

module.exports = app;
