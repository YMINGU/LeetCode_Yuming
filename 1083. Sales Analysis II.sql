# Write your MySQL query statement below
SELECT s.buyer_id FROM Sales s JOIN Product p ON s.product_id=p.product_id GROUP BY s.buyer_id HAVING GROUP_CONCAT(p.product_name) LIKE '%S8%' AND GROUP_CONCAT(p.product_name) NOT LIKE '%iPhone%'
