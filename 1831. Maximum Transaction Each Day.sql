# Write your MySQL query statement below
SELECT transaction_id FROM (SELECT *,DENSE_RANK()OVER(PARTITION BY day ORDER BY amount DESC)AS rnk
FROM Transactions)t WHERE rnk=1 ORDER BY 1
