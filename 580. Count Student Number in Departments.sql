# Write your MySQL query statement below
SELECT d.dept_name AS dept_name, COUNT(s.student_id) AS student_number FROM Department d LEFT OUTER JOIN Student s ON s.dept_id=d.dept_id GROUP BY d.dept_name ORDER BY 2 DESC, 1 ASC
