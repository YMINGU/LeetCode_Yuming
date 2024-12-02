CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT COUNT(DISTINCT user_id) AS user_cnt FROM Purchases WHERE time_stamp >=startDate AND time_stamp<=endDate AND amount>=minAmount
      
  );
END
