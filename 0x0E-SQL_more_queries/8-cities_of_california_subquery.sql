-- Lists all the cities of California that can be found in database hbtn_0d_usa
-- States table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY cities.id;
