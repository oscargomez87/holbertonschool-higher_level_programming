-- Creates the database hbtn_0d_usa and the table states
-- with value id INT unique, auto generated, not null and is a primary key
-- and name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL)
