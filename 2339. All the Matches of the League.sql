# Write your MySQL query statement below
SELECT e1.team_name AS home_team ,e2.team_name AS away_team FROM Teams e1 JOIN Teams e2 ON e1.team_name!=e2.team_name
