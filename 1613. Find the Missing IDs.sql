# Write your MySQL query statement below
WITH RECURSIVE seq(n) AS (SELECT 1 UNION ALL SELECT n+1 FROM seq WHERE n+1<=(SELECT MAX(Customer_id) FROM Customers))
SELECT n AS ids FROM seq WHERE n NOT IN (SELECT DISTINCT customer_id FROM Customers)
