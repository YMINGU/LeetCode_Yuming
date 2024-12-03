# Write your MySQL query statement below
SELECT CASE WHEN NY.e>CA.e THEN 'New York University' WHEN NY.e<CA.e THEN 'California University' ELSE 'No Winner' END AS winner FROM (SELECT COUNT(*) AS e FROM NewYork WHERE score>=90) AS NY,(SELECT COUNT(*) AS e FROM California WHERE score>=90) AS CA;
