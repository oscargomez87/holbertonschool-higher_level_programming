-- Lists the number of records with the same score in the table second_table
-- showing the score and averga as number ordered by number in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC
