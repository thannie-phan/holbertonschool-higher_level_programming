-- list records of second_table in database hbtn_0c_0
-- ordered by score (top first)
-- only show those with score >= 10

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
