# Write your MySQL query statement below
WITH cte AS(SELECT employee_id,name,salary FROM Employees WHERE salary IN (SELECT salary FROM Employees e
GROUP BY salary HAVING COUNT(salary)>1))
SELECT employee_id,name,salary,DENSE_RANK()OVER(ORDER BY salary)AS team_id FROM cte ORDER BY 3,1
