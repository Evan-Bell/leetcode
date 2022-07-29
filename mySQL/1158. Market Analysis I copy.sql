# Write your MySQL query statement below
SELECT
    user_id AS buyer_id,
    join_date, 
    COUNT(o.order_date) AS orders_in_2019
FROM users u LEFT JOIN
    orders o
    ON u.user_id = o.buyer_id
    AND YEAR(o.order_date) = '2019'
GROUP BY
    user_id
ORDER BY
    user_id
