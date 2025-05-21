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
const app = require('http');

app.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');
    const database = process.argv[2];
    const list = await countStudents(database);
    res.end(list);
  }
  res.end();
}).listen(1245);

module.exports = app;
