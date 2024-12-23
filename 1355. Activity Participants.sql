# Write your MySQL query statement below
WITH u AS (SELECT activity,COUNT(DISTINCT id) AS c FROM Friends GROUP BY activity) SELECT activity FROM u WHERE c NOT IN (SELECT MAX(c) FROM u) AND c NOT IN (SELECT MIN(c) FROM u)
