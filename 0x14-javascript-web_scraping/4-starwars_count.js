#!/usr/bin/node
//script that prints the number of movies

const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 200) {
    let count = 0;
    const results = JSON.parse(body).results;
    const people = '/api/people/18/';
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.find(add => add.includes(people))) {
	count++;
      }
    }
    console.log(count);
  }
});
