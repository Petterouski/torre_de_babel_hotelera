const { handleCreateUser } = require('../services/userService');

async function create(req, res) {
  try {
    const user = await handleCreateUser(req.body);
    res.status(201).json(user);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}

module.exports = { create };
// This code defines a controller function for creating a user.
// It uses the `handleCreateUser` service function to process the request and returns the created user in the response.
// If an error occurs, it logs the error and returns a 500 status with an error message.
// This allows for separation of concerns, where the controller handles HTTP requests and responses, while the service handles business logic.
// The controller is responsible for interacting with the service layer and formatting the response, while the service layer is responsible for the core business logic and data manipulation.
// This structure promotes a clean architecture and makes the codebase easier to maintain and test.