# Write your MySQL query statement below
SELECT login_date,COUNT(DISTINCT user_id) AS user_count FROM (SELECT user_id,MIN(activity_date) AS login_date FROM Traffic WHERE activity='login' GROUP BY user_id HAVING DATEDIFF('2019-06-30',MIN(activity_date))<=90) t0 GROUP BY login_date
