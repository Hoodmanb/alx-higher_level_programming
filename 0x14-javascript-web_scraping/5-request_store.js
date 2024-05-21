#!/usr/bin/node
// script that gets the contents of a webpage

const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err)console.log(err);
    });
  }
});
