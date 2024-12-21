# Write your MySQL query statement below
SELECT a.gender,a.day,SUM(b.score_points)AS total FROM Scores a JOIN Scores b ON a.gender=b.gender AND a.day>=b.day GROUP BY 1,2 ORDER BY 1,2
