import express from "express";
import "dotenv/config";
import "./connection.js";
import api from "./src/routes/api.js";

const app = express();

// settings
app.set("port", process.env.PORT);

// middlewares
app.use(express.static("./src/public"));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// routes
app.use("/api", api);
app.use((req, res, next) => {
  res.status(400).redirect("/404.html");
});

// server launch
app.listen(app.get("port"));
