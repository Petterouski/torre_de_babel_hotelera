const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: process.env.DB_NAME,
  port: process.env.DB_PORT,
});

module.exports = pool;
// This code sets up a connection pool to a PostgreSQL database using environment variables for configuration.
// It uses the 'pg' library to create a pool and exports it for use in other