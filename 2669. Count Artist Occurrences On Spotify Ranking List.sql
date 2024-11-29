# Write your MySQL query statement below
SELECT artist,COUNT(id) AS occurrences FROM Spotify GROUP BY artist ORDER BY 2 DESC,1 ASC
