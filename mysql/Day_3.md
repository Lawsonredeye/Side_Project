## Learning MySQL

so today i refreshed my learning first on the **SELECT** query and i also learnt how to use AS alias keyword for creating an alias to a name.

### How to create an Alias using AS

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

## How to use the LIKE keyword

The like keyword is a simpler version of using regular expression which can be used to find a characters or records when it comes to using mysql.

Some common characters used are:

1. % : matches any characters

## Resources

Here are the important resources i used while learning:

1. [Programming wit](https://www.youtube.com/watch?v=7S_tz1z_5bA&t=920s)
