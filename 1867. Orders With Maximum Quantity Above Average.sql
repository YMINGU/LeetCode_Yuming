# Write your MySQL query statement below
WITH cte AS(SELECT order_id,product_id,quantity,MAX(quantity)AS Maxq,SUM(quantity)/COUNT(product_id)AS Avgq
FROM OrdersDetails GROUp BY 1)
SELECT order_id FROM cte WHERE MAXq>(SELECT MAX(Avgq)FROM cte)
