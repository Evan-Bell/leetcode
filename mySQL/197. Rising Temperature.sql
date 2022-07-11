# Write your MySQL query statement below
SELECT Weather.id AS Id FROM Weather 
JOIN Weather w ON DATEDIFF(Weather.recordDate, w.recordDate) = 1
AND weather.Temperature > w.Temperature
