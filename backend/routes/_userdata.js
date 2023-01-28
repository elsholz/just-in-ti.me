const express = require("express");
const { Mongoose } = require("mongoose");
const { patchUserData } = require("../models/patch_userdata");
const { UserData } = require("../models/userdata");

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const _dataRoutes = express.Router();
const { checkJwt, HTTP204, HTTP404, HTTP400, HTTP500 } = require("../utils")

_dataRoutes.get("/api/_userdata", async (req, res) => {
    console.log("Getting userdata")
    console.log(req.auth.payload.sub)
    let userAuthId = req.auth.payload.sub

    if (userAuthId) {
        let userData = await UserData.findOne({
            _id: userAuthId
        })

        if (userData) {
            res.status(200).json(userData)
        } else {
            const newUser = new UserData({
                _id: userAuthId,
                hours: {},
            })
            newUser.save(function (err) {
                if (err) return HTTP500(res);
                res.status(201).json(newUser)
            });
        }
    } else HTTP400(res)
})

_dataRoutes.patch("/api/_userdata", async (req, res) => {
    let userAuthId = req.auth.payload.sub

    const year = req.body.year

    if (userAuthId) {
        const data = new patchUserData(req.body)
        const error = data.validateSync()

        if (error) {
            console.log('error validating! ', error)
        } else {
            let updateRes = await userData.updateOne({
                _id: userAuthId,
            }, {
                $set: { ["hours." + data.year + '.' + data.week]: data.hours },
            })
        }
    } else HTTP400(res)
})

_dataRoutes.delete("/api/_userdata", async (req, res) => {
    let userAuthId = req.auth.payload.sub

    if (userAuthId) {
        const deletionRes = await UserData.deleteOne({
            _id: userAuthId
        })
        if (deletionRes.deletedCount) {
            return HTTP204(res)
        } else {
            return HTTP404(res)
        }
    } else HTTP400(res)
})

module.exports = _dataRoutes;
