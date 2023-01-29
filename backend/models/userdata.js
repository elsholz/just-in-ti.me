const mongoose = require("mongoose");

// Define a schema
const Schema = mongoose.Schema;
const validator = require('validator')

const UserData = new Schema({
    _id: {
        type: String
    },
    hours: {
        type: Object
    },
    layout: {
        type: Object
    }
}, { collection: "userdata", minimize: false, versionKey: false });

module.exports = {
    UserData: mongoose.model('userdata', UserData)
}
