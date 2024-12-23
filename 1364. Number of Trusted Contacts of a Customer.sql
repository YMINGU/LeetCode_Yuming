# Write your MySQL query statement below
SELECT i.invoice_id,cust.customer_name,i.price, COUNT(DISTINCT c.contact_name) AS contacts_cnt,COUNT(DISTINCT name.customer_name) AS trusted_contacts_cnt FROM Invoices i LEFT JOIN Customers cust ON i.user_id=cust.customer_id LEFT JOIN Contacts c ON c.user_id=cust.customer_id LEFT JOIN Customers name ON name.customer_name=c.contact_name GROUP BY i.invoice_id 