-- script that displays the average temperature 
-- (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) as avg_temp FROM temperature ORDER BY avg_temp DESC;
