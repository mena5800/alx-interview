# Star Wars API Project

## Description

This project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. The project involves making HTTP requests, handling asynchronous operations, and processing JSON data in JavaScript.

## Learning Objectives

By the end of this project, you should be able to:

- Make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
- Understand and use the basics of RESTful APIs.
- Manage asynchronous operations with callbacks, promises, and async/await syntax.
- Handle API response data asynchronously.
- Parse and manipulate JSON data returned by APIs.
- Use command line arguments to pass data to a Node.js script.
- Iterate over arrays and manipulate data structures to format and display character names.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should be `semistandard` compliant
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## Installation

### Install Node 10

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install `semistandard`

```bash
$ sudo npm install semistandard --global
```

### Install `request` module

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Project Structure

- **GitHub Repository:** [alx-interview](https://github.com/alx-interview)
- **Directory:** `0x06-starwars_api`
  - **Files:**
    - `0-starwars_characters.js`

## Tasks

### 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: `3` = "Return of the Jedi"
- Display one character name per line in the same order as the "characters" list in the `/films/` endpoint
- You must use the Star Wars API
- You must use the `request` module

**File:** `0-starwars_characters.js`

**Example:**

```sh
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```
