#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

function fetchJson (url) {
  return new Promise((resolve, reject) => {
    request({ url, json: true }, (err, response, body) => {
      if (err) return reject(err);
      resolve(body);
    });
  });
}

async function getCharacters () {
  try {
    // Fetch film data
    const filmData = await fetchJson(url);

    if (!filmData || !filmData.characters) {
      console.error('Failed to retrieve characters');
      process.exit(1);
    }

    // Fetch character data sequentially
    for (const characterUrl of filmData.characters) {
      const characterData = await fetchJson(characterUrl);
      console.log(characterData.name);
    }
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
}

getCharacters();
