const { json } = require('body-parser'); // Fetching data from two endpoints. Arttu Kesanto 1900649.
const fetch = require('node-fetch')

let jsonPosts = [] // Testing, disregarded.

async function getUsers() {
    try {
        let response = await fetch('https://jsonplaceholder.typicode.com/users');
        let json = await response.json()
        let users = json
        return users
    } catch {
        console.log("Something went wrong...")
    }
}

async function getPosts() {
    try {
        let response = await fetch("https://jsonplaceholder.typicode.com/posts");
        let json = await response.json()
        const jsonPosts = json
        return jsonPosts
    } catch {
        console.log("Error happened.")
    }
}

function getPosts2() { // Testing a different way to do things.
    let httpPromise = fetch("https://jsonplaceholder.typicode.com/posts");
    let jsonPromise = httpPromise.then(response => response.json());
    let eventsPromise = jsonPromise.then(json => json.data)

    return eventsPromise
}

//console.log(getPosts2())


//const postData = getPosts();
//value = ''
//getUsers().then((value) => console.log(value))

//console.log(getPosts())
//console.log(getUsers())



module.exports = { getUsers, getPosts }