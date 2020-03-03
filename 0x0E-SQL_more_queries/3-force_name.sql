-- Creates the table force_name
-- with fields (id INT, name VARCHAR(256))
-- if the table already exists it doesn't fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
