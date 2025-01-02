# Write your MySQL query statement below
WITH temp AS(SELECT gold_medal AS user_id,contest_id,'gold'AS medal FROM Contests UNION ALL
SELECT silver_medal AS user_id,contest_id,'silver'AS medal FROM Contests UNION ALL
SELECT bronze_medal AS user_id,contest_id,'bronze'AS medal FROM Contests),
cond1 AS(SELECT DISTINCT user_id FROM temp WHERE (user_id,contest_id+1)IN (SELECT user_id,contest_id FROM temp)
AND(user_id,contest_id+2) IN (SELECT user_id,contest_id FROM temp)),
cond2 AS (SELECT user_id,medal FROM temp WHERE medal='gold' GROUP BY 1,2 HAVING COUNT(contest_id)>=3)
SELECT name,mail FROM Users WHERE user_id in (SELECT user_id FROM cond1 UNION SELECT user_id FROM cond2)
