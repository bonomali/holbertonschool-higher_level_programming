-- counts number of records with the same score
SELECT score, COUNT(*) number FROM second_table GROUP BY score DESC;
