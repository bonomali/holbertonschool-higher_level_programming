-- lists all records of second_table except those without a name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
