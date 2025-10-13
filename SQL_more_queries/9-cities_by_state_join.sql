-- lists all cities contained in the database hbtn_0d_usa
-- each record displays: cities.id - cities.name - states.name
-- JOIN connects cities to states via state_id. id in states is the same as state_id in cities so we can JOIN tables using this common column. 

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
