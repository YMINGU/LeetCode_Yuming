# Write your MySQL query statement below
SELECT left_operand,operator,right_operand,CASE WHEN operator='>' AND v0.value>v1.value THEN 'true' WHEN operator='<' AND v0.value<v1.value THEN 'true' WHEN operator='=' AND v0.value=v1.value THEN 'true' ELSE 'false' END AS value FROM Expressions e LEFT JOIN Variables v0 ON e.left_operand=v0.name LEFT JOIN Variables v1 ON e.right_operand=v1.name
