const { createServer } = require('node:http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;
const app = createServer(async (req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');

    return;
  }

  if (req.url === '/students') {
    try {
      const output = await countStudents('database.csv');
      res.statusCode = 200;
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

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
