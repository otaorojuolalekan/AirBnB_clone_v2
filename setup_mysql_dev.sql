-- this script prepares a MySQL server for the project
-- task: to create project db with name : hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create new user: hbnb_dev with all privileges
-- on the db hbnb_dev_db
-- with the password : hbnb_dev_pwd if it dosen't exist

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES; -- to persist to db

-- grant the SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES; -- to persist to db
