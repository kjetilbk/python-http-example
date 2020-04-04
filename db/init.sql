CREATE DATABASE flaskapp;
use flaskapp;

CREATE TABLE people (
    name VARCHAR(100),
    age int
);

INSERT INTO people (name, age) VALUES ("Kjetil", 27);