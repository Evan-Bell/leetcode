# Write your MySQL query statement below
SELECT
    DISTINCT stock_name,
    SUM(
        CASE
            WHEN operation LIKE 'Sell' THEN price
            ELSE -price
        END
    ) AS capital_gain_loss
FROM
    stocks
GROUP BY
    stock_name
