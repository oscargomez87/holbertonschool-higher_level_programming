-- Creates the database hbtn_0d_2 and the user user_0d_2
-- The user has only the SELECT privilege
-- Password is not set
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
