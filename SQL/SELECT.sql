SELECT * FROM tablename;

SELECT columnname, columnname FROM tablename;

SELECT columnname AS 'Alias' FROM tablename;

SELECT DISTINCT columnname FROM tablename;

SELECT * FROM tablename
WHERE columnname = condition;
-- = != < > <= >=

SELECT * FROM tablename
WHERE columnname LIKE 'Se_en';
-- _ is wildcard single character in pattern

SELECT * FROM tablename
WHERE columnname LIKE '%man%';
-- % is wildcard string in pattern (man is not case sensitive)

SELECT * FROM tablename
WHERE columnname IS NOT NULL;

SELECT * FROM tablename
WHERE columnname BETWEEN 'A' AND 'J';
-- J included, Just excluded

SELECT * FROM tablename
WHERE columnname < 1985
AND columnname = 'string';

SELECT * FROM tablename
WHERE columnname < 1985
OR columnname = 'string';

SELECT * FROM tablename
WHERE columnname < 1985
ORDER BY columnname DESC;
-- ORDER BY always after WHERE, DESC explicit ASC default

SELECT * FROM tablename
LIMIT 10;
-- LIMIT always goes at the very end of query

SELECT columnname,
CASE
WHEN condition THEN 'Result1'
WHEN othercondition THEN 'Result2'
ELSE 'Result3'
END
FROM tablename;
-- WHEN THEN behaves as else if (not if)

SELECT COUNT(columnname or *)
FROM tablename
WHERE condition;

SELECT SUM(columnname)
FROM tablename;

SELECT MAX(columnname)
FROM tablename;

SELECT MIN(columnname)
FROM tablename;

SELECT AVG(columnname)
FROM tablename;

SELECT ROUND(columnname, 2)
FROM tablename;

SELECT columnname, AVG(columnname)
FROM tablename
GROUP BY columnname;
-- GROUP BY comes after WHERE but before ORDER BY and LIMIT

SELECT columnname, AVG(columnname)
FROM tablename
GROUP BY 1
ORDER BY 2;

SELECT columnname, AVG(columnname)
FROM tablename
GROUP BY 1
HAVING AVG(columnname) > 5;
-- HAVING comes after GROUP BY but before ORDER BY and LIMIT

SELECT tablename.columnname, tablename.columnname
FROM tablename
JOIN tablename
ON tablename.columnname = tablename.columnname;
-- Simple join/inner join: only results matching ON condition

SELECT *
FROM tablename
LEFT JOIN tablename
ON tablename.columnname = tablename.columnname;

SELECT *
FROM tablename
CROSS JOIN tablename;

SELECT * FROM tablename
UNION
SELECT * FROM tablename;
-- same number and type of columns in both tables

WITH firstquery AS (
    SELECT columnname FROM tablename
)
SELECT *
FROM firstquery
JOIN secondtable
ON firstquery.columnname = secondtable.columnname;