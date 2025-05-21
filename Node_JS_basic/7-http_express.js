async function countStudents(path) {
  const fs = require('fs').promises;
  try {
    const data = await fs.readFile(path, 'utf-8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const students = lines.slice(1);

    let result = (`Number of students: ${students.length}\n`);

    const fieldGroups = {};

    students.forEach((student) => {
      const fields = student.split(',');
      const firstName = fields[0];
      const field = fields[3];

      if (!fieldGroups[field]) {
        fieldGroups[field] = [];
      }
      fieldGroups[field].push(firstName);
    });
    for (const field in fieldGroups) {
      const studentsList = fieldGroups[field].join(', ');
      result += (`Number of students in ${field}: ${fieldGroups[field].length}. List: ${studentsList}\n`);
    }
    result = result.trim();
    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const express = require('express');

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
