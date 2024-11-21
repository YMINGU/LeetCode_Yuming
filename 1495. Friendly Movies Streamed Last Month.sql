# Write your MySQL query statement below
SELECT DISTINCT c.title FROM Content c JOIN TVProgram t ON c.content_id=t.content_id WHERE c.Kids_content='Y' AND c.content_type='Movies' AND t.program_date BETWEEN '2020-06-01' AND '2020-06-30'
