const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  const database = process.argv[2];
  const list = await countStudents(database);
  res.send(`This is the list of our students\n${list}`);
});
app.listen(1245);
module.exports = app;
