# Write your MySQL query statement below
SELECT DISTINCT visited_on,SUM(amount)OVER w AS amount,ROUND((SUM(amount)OVER w)/7,2) AS average_amount FROM Customer WINDOW w AS(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 day PRECEDING AND CURRENT ROW) LIMIT 6,999
