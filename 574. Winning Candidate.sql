# Write your MySQL query statement below
SELECT c.name FROM Candidate c JOIN (SELECT candidateId,COUNT(*) AS count FROM Vote GROUP BY candidateId ORDER BY COUNT(*) DESC LIMIT 1) v ON c.id=v.candidateId
