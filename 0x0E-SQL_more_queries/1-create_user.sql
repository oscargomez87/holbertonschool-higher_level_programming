-- Creates the MySQL server user user_0d_1 with all privileges
-- password is set to user_0d_1_pwd and if the user already exists it's skipped
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
