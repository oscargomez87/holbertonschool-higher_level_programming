-- Creates the table unique_id on your MySQL server
-- with the fields id of type int default value 1 and unique
-- and name of type varchar max 256 chars
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256))
