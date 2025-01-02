# Write your MySQL query statement below
SELECT user_id,MAX(w) biggest_window FROM (SELECT user_id,abs(DATEDIFF(visit_date,IFNULL(LEAD(visit_date)
OVER(PARTITION BY user_id ORDER BY visit_date),'2021-1-1')))w FROM UserVisits)t GROUP BY user_id ORDER BY 1
