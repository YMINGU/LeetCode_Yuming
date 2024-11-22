# Write your MySQL query statement below
SELECT SUBSTRING(order_date,1,7) AS month,COUNT(order_id) AS order_count,COUNT(DISTINCT customer_id) AS customer_count FROM Orders WHERE invoice>20 GROUP BY month
