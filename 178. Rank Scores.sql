# Write your MySQL query statement below
SELECT s.score,COUNT(DISTINCT t.score) AS 'rank' FROM Scores s INNER JOIN Scores T ON s.score<=t.score GROUP BY s.id,s.score ORDER BY s.score DESC
