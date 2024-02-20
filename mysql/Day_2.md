# Day 2 of Learning MySql

I learnt more about the basic commands on how to create a database, table and how to revoke access as well as grant access to a user specifying what kind of access the user is able to use in a specific database or table.

The **Data Control Language** is extremely powerful command in which Database admin can use. The DCL is best for controlling who has certain previleges to a database to prevent data theft, deleting of the entire database by a novice.

To use the DCL command like GRANT and REVOKE you can follow this syntax;
1. create the user
CREATE USER <NAME>@<IP_ADDRESS> IDENTIFIED BY <PASSWORD>
`CREATE USER "redeye"@"localhost" IDENTIFIED BY "pass"`

2. To delete users use the DROP command.
`DROP USER <USERNAME>@<IP_ADDRESS>`
`DROP USER "redeye"@"localhost";`

3. GRANT PRIVILEGE ON <DATABASE_NAME.TABLE_NAME>TO <USER_@_IP_ADDRESS>
`GRANT SELECT ON my_data_base.school_table TO 'redeye'@'localhost';`

The **Data Manipulation Language** is used for manipulation of data which consist of the Select, Insert, Update and Delete command which is used to alter the data in a database table easily.

1. `SELECT * FROM <TABLE_NAME>;` : prints all details in a table

2. `INSERT INTO <TABLE_NAME> VALUE <VALUE_1, ...>;` : inserts data into a database table without specifying all the columns

3. UPDATE <TABLE_NAME> SET <COLUMN_VALUE> = <DATA_TYPE> WHERE <CONDITION> : updates the table column
`UPDATE law_table SET name = 'lawson' WHERE id = 100;`

4. DELETE FROM <TABLE_NAME> WHERE <CONDITION>: used to delete values from table using a specific condition.
`DELETE FROM law_table WHERE age = 32;`

**BONUS**
To write a sql script and run from your server follow this steps;
0. Navigate to the folder of your sql script
1. `sudo mysql` <!-- login into your sql server -->
2. `SOURCE <NAME_OF_SQL_SCRIPT.sql>;`

## Video and Resources
[Basic MySQL commands](https://youtu.be/cWMCHbxMiMI?si=fNSZfn9RKzee1iim)
[How To create and deleter User](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)