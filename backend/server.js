// Loads the configuration from config.env to process.env

const compression = require("compression");
const express = require("express");
// const cors = require("cors");
// get MongoDB driver connection
const dbo = require("./db/conn");
const { checkJwt } = require("./utils");

const PORT = 3000;
const app = express();

const utils = require("./utils")

//app.use(cors());
app.use(express.json());

// USE COMPRESSION
app.use(compression());

// Only allow authenticated requests
app.use(checkJwt);

// Routes:
app.use(require("./routes/_userdata"));

// FOR TESTING: Disable Caching
app.disable('etag');

// perform a database connection when the server starts
dbo.connectToServer(function (err) {
  if (err) {
    console.error(err);
    process.exit();
  }

  // start the Express server
  app.listen(PORT, () => {
    console.log(`Server is running on port: ${PORT}`);
  });
});
