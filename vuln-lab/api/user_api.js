const express = require("express");
const app = express();

app.get("/user", (req, res) => {
    const id = req.query.id;
    res.send("User data for ID: " + id);
});

app.listen(3000);
