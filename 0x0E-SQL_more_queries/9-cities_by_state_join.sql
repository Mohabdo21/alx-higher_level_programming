-- Select all cities and their corresponding state names from the cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
