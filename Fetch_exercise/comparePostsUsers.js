// File for comparing users and posts. Arttu Kesanto, 1900649.
const { getUsers, getPosts } = require('./fetchData') // Creating "imports" from the fetchData.js-file.


async function postsByUsers() {
    let users = await getUsers(); // Getting users.
    let posts = await getPosts(); // Getting posts.

    let users2 = users.map(user => user) // Debugging and mapping.
    let posts2 = posts.map(post => post) // Debugging and mapping.


    let list = users.map(function (user) { // Mapping the users and filtering posts to a desired user. Returning a new list with wanted items.
        return {
            ...user,
            post: posts.filter(
                post => post.userId === user.id) // Filtering the wanted posts by IDs from both lists. Creating new attribute, spreading method.
        };
    });
    console.log(list)



    /*list.forEach(user => {
        user.post = 
        (posts.forEach(post => function(post) {
            if (post.userId === user.id) {
                return post
            }
        }))
    }); */

    /*for (i=0; i < users2.length; i++) {
        userID = users2[i].id
        for (i=0; i < posts2.length; i++) {
            if (userID == posts2[i].userId) {
                console.log("success")
                postObject = posts2[i]
                return {...users2, post:{postObject}}
            }
            
        }

    } */

    console.log(users2)

    return list // Returning the list so that it can be sent to the localhost as JSON.
}

// console.log(users2)

console.log(postsByUsers()) // Debugging with the actual return file, can now see users2 from console.log for example.


module.exports = { postsByUsers } // Exporting to the server.js-file.