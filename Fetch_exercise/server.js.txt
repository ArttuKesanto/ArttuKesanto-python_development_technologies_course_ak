// Node server.js starts the desired modules and this one; print can be found as JSON on localhost:3000. Arttu Kesanto, 1900649.
const express = require('express');
const app = express();

const { postsByUsers } = require('./comparePostsUsers')

app.get('/', async function (req, res) {
    let posts = await postsByUsers(); // Getting posts from the file comparePostsUsers.js.
    //let users = await getUsers();

    //let matched = {}

    res.json(posts); // Sending to the localhost:3000/.
})



app.listen(3000, () => console.log('Running as intended...'));