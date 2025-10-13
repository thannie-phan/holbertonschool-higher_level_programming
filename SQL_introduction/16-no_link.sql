-- list all records in table second_table of database hbtn_0c_0
-- don't list rows where name does not have value
-- list by DESC score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;