# Write your MySQL query statement below
SELECT f.followee AS follower,COUNT(*) AS num FROM Follow f WHERE f.followee IN (SELECT DISTINCT follower FROM Follow) GROUP BY 1 ORDER BY 1
