const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const students = lines.slice(1);

    const result = {};

    for (const student of students) {
      const fields = student.split(',');
      if (fields.length >= 4) {
        const firstName = fields[0].trim();
        const field = fields[3].trim();

        if (!result[field]) {
          result[field] = [];
        }

        result[field].push(firstName);
      }
    }

    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = readDatabase;
