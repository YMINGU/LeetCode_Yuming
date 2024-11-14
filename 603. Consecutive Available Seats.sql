# Write your MySQL query statement below
SELECT DISTINCT a.seat_id FROM Cinema a JOIN Cinema b ON abs(a.seat_id-b.seat_id)=1 WHERE a.free=True AND b.free=True ORDER BY a.seat_id
