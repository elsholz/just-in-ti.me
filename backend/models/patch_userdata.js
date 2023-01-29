const mongoose = require("mongoose");

// Define a schema
const Schema = mongoose.Schema;
// const validator = require('validator')

const hoursSchema = new Schema({
    from: {
        type: Number,
    },
    to: {
        type: Number,
    },
    description: {
        type: String,
        validator: function (v) {
            const re = /^.{0,100}$/
            return re.test(v)
        }
    },
}, { _id: undefined })

const patchUserDataSchema = new Schema({
    year: {
        type: String,
        validator: function (v) {
            const re = /^\d{4}$/
            return re.test(v)
        },
        message: 'Year is invalid'
    },
    month: {
        type: String,
        validator: function (v) {
            var re = /^\d{2}$/;
            return re.test(v)
        },
        message: 'Month is invalid'
    },
    day: {
        type: String,
        validator: function (v) {
            var re = /^\d{2}$/;
            return re.test(v)
        },
        message: 'Day is invalid'
    },
    hours: {
        type: [hoursSchema],
    },
}, { collection: "userdata", minimize: false, versionKey: false });

module.exports = {
    patchUserData: mongoose.model('patchUserData', patchUserDataSchema)
}
