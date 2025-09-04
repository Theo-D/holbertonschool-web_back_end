const { createServer } = require('node:http');
const countStudents = require('./3-read_file_async');

const port = 1245;
const db = process.argv[2];
const app = createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/' && req.method === 'GET') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');

    return;
  }

  if (req.url === '/students' && req.method === 'GET') {
    try {
      res.statusCode = 200;
      const output = await countStudents(db);
      res.end(`This is the list of our students\n${output}`);
    } catch (err) {
      res.statusCode = 404;
      res.end('Cannot load the database');
    }

    return;
  }

  res.statusCode = 404;
  res.end('Not Found');
});

app.listen(port);

module.exports = app;
