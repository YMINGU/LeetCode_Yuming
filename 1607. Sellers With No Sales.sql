# Write your MySQL query statement below
SELECT s.seller_name AS seller_name FROM Seller s LEFT JOIN Orders o ON s.seller_id=o.seller_id GROUP BY s.seller_id HAVING SUM(IFNULL(YEAR(sale_date)='2020',0))=0 ORDER BY 1 ASC
