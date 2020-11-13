/**
 * webpack configuration for httpwatcher
 */

var path = require("path");

module.exports = {
  entry: "./httpwatcher.js",
  output: {
    path: path.resolve(__dirname, "build"),
    filename: "httpwatcher.bundle.js",
  },
};
