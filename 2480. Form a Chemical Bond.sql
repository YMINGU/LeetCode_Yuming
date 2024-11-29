# Write your MySQL query statement below
SELECT a.symbol AS metal,b.symbol AS nonmetal FROM Elements a,Elements b WHERE a.type='Metal' AND b.type='Nonmetal'
