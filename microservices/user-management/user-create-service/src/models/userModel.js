const db = require('../config/db');

async function createUser(user) {
  const { name, email } = user;
  const res = await db.query('INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *', [name, email]);
  return res.rows[0];
}

module.exports = { createUser };
// This code defines a function to create a user in the database.
// It uses a PostgreSQL database connection pool to execute an INSERT query and returns the created user