# Write your MySQL query statement below
SELECT company_id,employee_id,employee_name,ROUND(salary*(1-tax),0) AS salary FROM
Salaries LEFT JOIN (SELECT company_id,IF(MAX(salary)<1000,0,IF(MAX(salary)<=10000,0.24,0.49))AS tax
FROM Salaries GROUP BY 1) a USING (company_id)
