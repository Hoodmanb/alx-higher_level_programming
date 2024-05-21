#!/usr/bin/node
// script that prints the title of a Star Wars movie

const request = require('request');
const requireUrl = 'https://swapi-api.alx-tools.com/api/films/';
request(requireUrl + process.argv[2], (err, response, body) => {
  if (err)console.log(err);
  else console.log(JSON.parse(body).title);
});
