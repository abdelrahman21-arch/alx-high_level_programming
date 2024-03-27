#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
	if (!error) {
	  const content = JSON.parse(body);
	  let characters = content.characters;
		printCharacters(characters, 0);
	}
	else {
		console.log(error);
	}
});

function printCharacters (characters, index) {
	request(characters[index], function (error, response, body) {
		if (!error) {
			console.log(JSON.parse(body).name);
			if (index + 1 < characters.length) {
				printCharacters(characters, index + 1);
			}
		}
		else {
			console.log(error);
		}
	});
}
