// Arttu Kesanto, 1900649, Haaga-Helian kampus
//import Redux from 'redux'

const Redux = require('redux')

function addColor(value) {
    return {
        type: "ADD",
        color: value
    };
}

function removeColor(value) {
    return {
        type: "REMOVE",
        color: value
    };
}

function favoriteColors(state, action) {
    if (state == undefined) {
        state = []
    }

    if (action.type === "ADD") {
        return state.concat(action.color);
    } else if (action.type === "REMOVE") {
        //return state.filter(item => item !== action.color) // The first item is the item(s) in the list, and that item cannot be what is given. Filter creates a new list, array.
        return state.filter(function (e) { // Can also be done like this.
            return e !== action.color
        })
    } else {
        return state;
    }
}

// Creating a REDUX container. Added some colours for testing.
let store = Redux.createStore(favoriteColors);
store.dispatch(addColor("sininen"));
store.dispatch(addColor("sininen"));
store.dispatch(addColor("sininen"));
store.dispatch(addColor("keltainen"));
store.dispatch(addColor("vihreä"));
store.dispatch(addColor("vihreä"));
store.dispatch(addColor("vihreä"));
store.dispatch(removeColor("sininen"));

console.log(store.getState()); //pitäisi tulla tuloste ['keltainen', 'vihreä']

