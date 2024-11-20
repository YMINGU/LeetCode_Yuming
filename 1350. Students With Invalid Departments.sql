# Write your MySQL query statement below
SELECT id,name FROM Students s WHERE department_id NOT IN (SELECT id FROM Departments)
