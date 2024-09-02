#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach(url => {
      request(url, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
