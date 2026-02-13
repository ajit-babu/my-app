const express = require('express');
const os = require('os');

const app = express();

app.get('/', (req, res) => {
  res.send(`
    <h2>DevOps CI/CD Working 🚀</h2>
    <p>Hostname: ${os.hostname()}</p>
  `);
});

app.listen(3000, () => {
  console.log("App running on port 3000");
});
