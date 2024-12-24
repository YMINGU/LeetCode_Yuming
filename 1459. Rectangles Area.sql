# Write your MySQL query statement below
SELECT po1.id AS p1,po2.id AS p2,abs((po1.x_value-po2.x_value)*(po1.y_value-po2.y_value))AS area FROM Points po1 INNER JOIN Points po2 ON po2.id>po1.id HAVING area!=0 ORDER BY 3 DESC,1,2
