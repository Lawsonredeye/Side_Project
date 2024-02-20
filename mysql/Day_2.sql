-- Task:

-- SELECT Statement: Write a query to retrieve all data from the table you created on Day 1. Experiment with different clauses like WHERE and ORDER BY.
SELECT * FROM days_of_mysql;

SELECT * FROM days_of_mysql
WHERE id < 0
ORDER BY id ASC;

-- INSERT Statement: Add a few more rows to your table using the INSERT statement.

INSERT INTO days_of_mysql
VALUE (3, 'OSCAR', 43),
(4, 'LEWIS', 28),
(5, 'HAMILTON', 28),
(6, 'TRAVIS', 25),
(7, 'BAKER', 29);

-- UPDATE Statement: Modify the values of a specific row using the UPDATE statement.
UPDATE days_of_mysql
SET name = 'MC-QUEEN'
WHERE age = 29;

-- DELETE Statement: Remove a row from your table using the DELETE statement.
DELETE FROM days_of_mysql
WHERE id = 4;