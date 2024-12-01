# Write your MySQL query statement below
SELECT DISTINCT a.user_id FROM Confirmations a,Confirmations b WHERE a.user_id=b.user_id AND a.time_stamp<b.time_stamp AND a.time_stamp>=date_sub(b.time_stamp,interval 24 hour)
