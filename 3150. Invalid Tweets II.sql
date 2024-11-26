# Write your MySQL query statement below
SELECT tweet_id FROM (SELECT tweet_id,content,CASE WHEN content>=140 then False WHEN content like "%@%@%@%@%" THEN False WHEN content like "%#%#%#%#%" THEN False ELSE True END AS valid FROM Tweets) a WHERE valid=False 
