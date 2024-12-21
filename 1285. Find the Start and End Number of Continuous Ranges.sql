# Write your MySQL query statement below
SELECT MIN(log_id)AS start_id,MAX(log_id)AS end_id FROM (SELECT log_id,row_number() OVER(ORDER BY log_id) AS rn FROM Logs)a GROUP BY log_id-rn
