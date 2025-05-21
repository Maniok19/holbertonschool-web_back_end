const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2];
    const list = await countStudents(database);
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write(`This is the list of our students\n${list}`);
    res.end();
  }
  res.end();
});
app.listen(1245);

module.exports = app;
