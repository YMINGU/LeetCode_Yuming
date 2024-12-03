# Write your MySQL query statement below
SELECT session_id FROM Playback p LEFT JOIN Ads a ON p.customer_id=a.customer_id AND timestamp BETWEEN start_time AND end_time WHERE timestamp IS NULL
