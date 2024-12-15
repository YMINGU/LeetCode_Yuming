# Write your MySQL query statement below
SELECT a.id,IF(ISNULL(a.p_id),'Root',IF(a.id IN (SELECT p_id FROM Tree),'Inner','Leaf'))Type FROM Tree a ORDER BY a.id
