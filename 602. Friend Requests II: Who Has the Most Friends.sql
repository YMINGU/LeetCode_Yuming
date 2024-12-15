# Write your MySQL query statement below
WITH all_ids AS (SELECT requester_id AS id FROM RequestAccepted UNION ALL SELECT accepter_id AS id FROM RequestAccepted) SELECT id,COUNT(id) AS num FROM all_ids GROUP BY id ORDER BY 2 DESC LIMIT 1
