# Write your MySQL query statement below
SELECT DISTINCT p.product_name,p.product_id,o.order_id,o.order_date FROM Products p JOIN
(SELECT order_id,order_date,product_id,RANK()OVER(PARTITION BY product_id ORDER BY order_date DESC)AS rnk FROM Orders)o
ON p.product_id=o.product_id AND rnk=1 ORDER BY 1,2,3
