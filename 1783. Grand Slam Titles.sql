# Write your MySQL query statement below
WITH cte AS ((SELECT Wimbledon AS id FROM championships)UNION ALL (SELECT Fr_open AS id FROM championships)
UNION ALL (SELECT US_open AS id FROM championships)UNION ALL (SELECT Au_open AS id FROM championships))
SELECT id AS player_id,player_name,COUNT(*)AS grand_slams_count FROM cte JOIN Players p ON cte.id=p.player_id GROUP BY 1
