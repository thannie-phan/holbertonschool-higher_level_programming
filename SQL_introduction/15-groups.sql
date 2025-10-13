-- list all records with the same score in table second_table of database hbtn_0c_0
-- display no of records with label number

SELECT score, COUNT (*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;