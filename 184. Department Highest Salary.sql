# Write your MySQL query statement below
SELECT d.name AS Department,e.name AS Employee,Salary FROM  Employee e JOIN Department d ON e.departmentId=d.id WHERE (e.DepartmentId,Salary) IN (SELECT DepartmentId,MAX(Salary) FROM Employee GROUP BY DepartmentId)
