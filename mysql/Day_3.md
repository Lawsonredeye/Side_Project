# Learning MySQL

so today i refreshed my learning first on the **SELECT** query and i also learnt how to use AS alias keyword for creating an alias to a name.

## How to create an Alias using AS

To create an ALIAS for any keyword or column name use the AS keyword in this way;
`SELECT first_name AS 'First Name';`
`SELECT points AS pts;`

## Using REGEX with mysql

Regular expressions **(REGEXP)** can actually be found every where in many programming language and tech stacks too and mysql is no different.

I learnt how to use regular expression using the following metacharacters on MySQL queries
SELECT column1, column2 ...
FROM table
WHERE column1 REGEXP '[a-z]|'; <!-- which means a-z or (|) means Logical OR -->

**common REGEXP metacharacters used in MySQL:**

1. | : means logical OR
2. ^a : means any word beginning with the character a
3. a$ : any word ending with the character a
4. [a-z]: any word that begins from a-z
5. [0-9]: any number from 0-9
6. . : matches all characters
7. \. : matches only dots (.)

There are more than these but these are the most used and most common regex in mySQL.

## LIKE OPERATOR

The like keyword is a simpler version of using regular expression which can be used to find a characters or records when it comes to using mysql.

Some common characters used are:

1. %b : matches all characters that ends with the letter b
   `SELECT * FROM customers where last_name LIKE '%b';`
2. %b%: matches all characters or records that begins or ends with the letter b
   `SELECT * FROM customers where last_name LIKE '%b%';`
3. \_c: matches with 2 letter words that ends with the letter c. Note that the amount of underscore must match with the word youre looking for from the specified record.
   `SELECT * FROM customers where last_name LIKE '__b';`

`SELECT * FROM customers where last_name LIKE '%b%';`
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+
| customer_id | first_name | last_name | birth_date | phone | address | city | state | points |
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+
| 2 | Ines | Brushfield | 1986-04-13 | 804-427-9456 | 14187 Commercial Trail | Hampton | VA | 947 |
| 3 | Freddi | Boagey | 1985-02-07 | 719-724-7869 | 251 Springs Junction | Colorado Springs | CO | 2967 |
| 4 | Ambur | Roseburgh | 1974-04-14 | 407-231-8017 | 30 Arapahoe Terrace | Orlando | FL | 457 |
| 5 | Clemmie | Betchley | 1973-11-07 | NULL | 5 Spohn Circle | Arlington | TX | 3675 |
| 8 | Thacher | Naseby | 1993-07-17 | 941-527-3977 | 538 Mosinee Center | Sarasota | FL | 205 |
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+

## BETWEEN OPERATOR

The between keyword can be used as if its a range to get records or rows that falls within the range of the specified values and it helps in making your queries neat by preventing using much OR operator on queries.
`SELECT * FROM customers WHERE points BETWEEN 900 AND 2000;`
+-------------+------------+------------+------------+--------------+------------------------+-----------+-------+--------+
| customer_id | first_name | last_name | birth_date | phone | address | city | state | points |
+-------------+------------+------------+------------+--------------+------------------------+-----------+-------+--------+
| 2 | Ines | Brushfield | 1986-04-13 | 804-427-9456 | 14187 Commercial Trail | Hampton | VA | 947 |
| 7 | Ilene | Dowson | 1964-08-30 | 615-641-4759 | 50 Lillian Crossing | Nashville | TN | 1672 |
| 9 | Romola | Rumgay | 1992-05-23 | 559-181-3744 | 3520 Ohio Trail | Visalia | CA | 1486 |
+-------------+------------+------------+------------+--------------+------------------------+-----------+-------+--------+

## ORDER BY OPERATOR

The order by clause is used in the case of arranging/sorting the output in ascending (ASC) or descending (DESC) order.
It can be written in this syntax:
`SELECT * FROM customers WHERE points > 945 ORDER BY points DESC;`
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+
| customer_id | first_name | last_name | birth_date | phone | address | city | state | points |
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+
| 5 | Clemmie | Betchley | 1973-11-07 | NULL | 5 Spohn Circle | Arlington | TX | 3675 |
| 6 | Elka | Twiddell | 1991-09-04 | 312-480-8498 | 7 Manley Drive | Chicago | IL | 3073 |
| 3 | Freddi | Boagey | 1985-02-07 | 719-724-7869 | 251 Springs Junction | Colorado Springs | CO | 2967 |
| 1 | Babara | MacCaffrey | 1986-03-28 | 781-932-9754 | 0 Sage Terrace | Waltham | MA | 2273 |
| 7 | Ilene | Dowson | 1964-08-30 | 615-641-4759 | 50 Lillian Crossing | Nashville | TN | 1672 |
| 9 | Romola | Rumgay | 1992-05-23 | 559-181-3744 | 3520 Ohio Trail | Visalia | CA | 1486 |
| 2 | Ines | Brushfield | 1986-04-13 | 804-427-9456 | 14187 Commercial Trail | Hampton | VA | 947 |
+-------------+------------+------------+------------+--------------+------------------------+------------------+-------+--------+

## IN OPERATOR

This is like a shortcut for the OR operator and it helps in creating cleaner and understandable queries to fetch records. It's really easy to use and it generally better when writing multiple OR.
`SELECT * FROM order_items WHERE product_id IN (2, 6, 10);`
+----------+------------+----------+------------+
| order_id | product_id | quantity | unit_price |
+----------+------------+----------+------------+
| 5 | 2 | 3 | 9.89 |
| 6 | 2 | 4 | 3.28 |
| 2 | 6 | 2 | 2.94 |
| 9 | 6 | 5 | 7.28 |
| 4 | 10 | 7 | 6.40 |
+----------+------------+----------+------------+

## IS NULL

This is used for checking records with no values at all and it is accompanied by the WHERE operator in some cases but other cases its used along side when creating columns.
`SELECT * FROM orders WHERE shipper_id IS NULL;`
+----------+-------------+------------+--------+-----------------------------------------------------------------------+--------------+------------+
| order_id | customer_id | order_date | status | comments | shipped_date | shipper_id |
+----------+-------------+------------+--------+-----------------------------------------------------------------------+--------------+------------+
| 1 | 6 | 2019-01-30 | 1 | NULL | NULL | NULL |
| 3 | 8 | 2017-12-01 | 1 | NULL | NULL | NULL |
| 4 | 2 | 2017-01-22 | 1 | NULL | NULL | NULL |
| 6 | 10 | 2018-11-18 | 1 | Aliquam erat volutpat. In congue. | NULL | NULL |
| 8 | 5 | 2018-06-08 | 1 | Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. | NULL | NULL |
+----------+-------------+------------+--------+-----------------------------------------------------------------------+--------------+------------+

IS NOT NULL is the inverse of the IS NULL operator.

## Resources

Here are the important resources i used while learning:

1. [Programming wit](https://www.youtube.com/watch?v=7S_tz1z_5bA&t=920s)

I hope someone foubd this documentation useful. Feel free to add what youve learnt here and keep pushing forward.
Remember it gets easy everyday but the hard part is doing it every single day. HAPPY CODING 🧑🏾‍💻.
