-- Task: 

-- Install MySQL on your machine.
-- Create a simple database and a table with a few columns.

CREATE DATABASE IF NOT EXISTS days_of_mysql;
USE days_of_mysql;
CREATE TABLE IF NOT EXISTS days_of_mysql (id INT, name VARCHAR(256), age INT);
DESCRIBE days_of_mysql;