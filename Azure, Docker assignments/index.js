// Example modified from https://github.com/mqttjs/MQTT.js#example
const mqtt = require('mqtt');

// Vehicle positioning for ongoing buses at Lauttasaari bridge
const myTopic = '/hfp/v2/journey/ongoing/vp/bus/+/+/+/+/+/+/+/+/60;24/18/69/27/#';

const hslClient = mqtt.connect('mqtts://mqtt.hsl.fi:8883'); // Opening up the connection.
const mosquittoClient = mqtt.connect('mqtt://test.mosquitto.org:1883'); // Opening up the connection.

hslClient.on('connect', function () { // Testing if connected and displaying messages accordingly.
    hslClient.subscribe(myTopic, function (err) {
        if (!err) {
            console.log('Connected!');
        } else {
            console.log(err);
        }
    })
});

hslClient.on('message', function (topic, message) { // Handled publishing here based on the speed.

    console.log(message.toString());
    let json = JSON.parse(message.toString());
    let speed = json.VP.spd; // Using this value for IF-statements.

    if (speed < 5.0) {
        let myMessage = { // Could do without "".
            "oper": json.VP.oper,
            "veh": json.VP.veh,
            "lat": json.VP.lat,
            "long": json.VP.long,
            "spd": json.VP.spd,
            "cause": "Potential traffic jam! Stay safe!"
        }

        mosquittoClient.publish('/swd4tn023/arttukesanto/traffic/jam', JSON.stringify(myMessage));
    } else if (speed > 8.33) { // Speed over 30 km/h.
        let myMessage = { // Could do without "".
            "oper": json.VP.oper,
            "veh": json.VP.veh,
            "lat": json.VP.lat,
            "long": json.VP.long,
            "spd": json.VP.spd,
            "cause": "Potential speeding!"
        }

        mosquittoClient.publish('/swd4tn023/arttukesanto/traffic/speed', JSON.stringify(myMessage));
    }

    console.log('Speed: ' + speed); // DEBUGGING.
})
