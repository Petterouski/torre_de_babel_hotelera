const { createUser } = require('../models/userModel');

async function handleCreateUser(data) {
  return await createUser(data);
}

module.exports = { handleCreateUser };
// This code defines a service function to handle user creation.
// It imports the `createUser` function from the user model and exports a function that calls it with the provided data.
// This allows for separation of concerns, where the service layer handles business logic and the model layer