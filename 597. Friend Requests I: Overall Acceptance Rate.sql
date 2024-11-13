SELECT IFNULL(
    (SELECT ROUND(COUNT(DISTINCT requester_id, accepter_id) /COUNT(DISTINCT sender_id, send_to_id), 2) FROM FriendRequest, RequestAccepted),0) AS accept_rate
