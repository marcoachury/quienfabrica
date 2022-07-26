import mongoose from "mongoose";

const { username, password, database } = {
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE
};

const MONGO_URL = `mongodb://${username}:${password}@cluster0-shard-00-00.bmkuc.mongodb.net:27017,cluster0-shard-00-01.bmkuc.mongodb.net:27017,cluster0-shard-00-02.bmkuc.mongodb.net:27017/${database}?ssl=true&replicaSet=atlas-83zvm0-shard-0&authSource=admin&retryWrites=true&w=majority`;

export default await mongoose.connect(MONGO_URL);
