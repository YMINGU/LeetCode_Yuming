# Write your MySQL query statement below
SELECT user_id,user_name,(credit-IFNULL(out_cash,0)+IFNULL(in_cash,0))AS credit,
IF((credit-IFNULL(out_cash,0)+IFNULL(in_cash,0))<0,'Yes','No') AS credit_limit_breached
FROM Users u LEFT JOIN (SELECT paid_by,SUM(amount)AS out_cash FROM Transactions GROUP BY paid_by) o
ON u.user_id=o.paid_by LEFT JOIN (SELECT paid_to,SUM(amount)AS in_cash FROM Transactions GROUP BY paid_to)i
ON u.user_id=i.paid_to
