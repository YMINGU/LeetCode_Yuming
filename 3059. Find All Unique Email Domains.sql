# Write your MySQL query statement below
SELECT SUBSTRING_INDEX(e.email,'@',-1) AS email_domain, COUNT(*) AS count FROM Emails e GROUP BY 1 having email_domain LIKE '%.com' ORDER BY 1 ASC
