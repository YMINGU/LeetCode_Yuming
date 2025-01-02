# Write your MySQL query statement below
WITH cte AS(SELECT IFNULL(b.apple_count,0)+IFNULL(c.apple_count,0)AS total_apples,
IFNULL(b.orange_count,0)+IFNULL(c.orange_count,0)AS total_oranges FROM Boxes b LEFT JOIN Chests c
ON b.chest_id=c.chest_id)
SELECT SUM(total_apples)AS apple_count,SUM(total_oranges)AS orange_count FROM cte
