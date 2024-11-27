# Write your MySQL query statement below
SELECT ABS((SELECT MAX(salary) FROM Salaries WHERE department='Marketing')-(SELECT MAX(salary) FROM Salaries WHERE department='Engineering')) AS salary_difference
