# Write your MySQL query statement below
SELECT a.name AS Employee FROM Employee a JOIN Employee b ON a.ManagerId=b.Id AND a.Salary>b.Salary;
