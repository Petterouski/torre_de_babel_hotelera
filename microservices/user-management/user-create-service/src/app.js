const express = require('express');
const { create } = require('./controllers/userController');
const app = express();

app.use(express.json());

app.post('/users', create);

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`user-create-service running on port ${port}`);
});
// This code sets up an Express.js application for the user creation service.
// It imports the user controller and defines a route for creating users.