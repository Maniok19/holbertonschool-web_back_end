const app = require('http');

app.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.send('Hello Holberton School!');
})
app.listen(1245);
module.exports = app;
