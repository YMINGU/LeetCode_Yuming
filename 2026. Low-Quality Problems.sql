# Write your MySQL query statement below
SELECT problem_id FROM Problems WHERE IFNULL(likes/(likes+dislikes),0)<0.6 ORDER BY problem_id ASC
