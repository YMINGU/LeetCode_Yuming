# Write your MySQL query statement below
WITH income_table AS(SELECT account_id,DATE_FORMAT(day,'%Y%m')AS months,SUM(amount)AS total_income FROM
Transactions WHERE type='Creditor' GROUP BY account_id,DATE_FORMAT(day,'%Y%m')),
t AS(SELECT i.account_id,months,total_income,max_income,LEAD(months,1)OVER(PARTITION BY account_id
ORDER BY months)AS next_month FROM income_table i JOIN Accounts a ON i.account_id=a.account_id WHERE total_income>max_income)
SELECT DISTINCT(account_id) FROM t WHERE next_month-months=1
