-- Creates the database hbtn_0d_usa and the table cities
-- id INT unique, auto generated, not null and is a primary key
-- state_id INT, not null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256),
       FOREIGN KEY(state_id) REFERENCES states(id)
);
