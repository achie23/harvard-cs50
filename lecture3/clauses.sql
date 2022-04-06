-- for flights TABLE
SELECT * FROM flights LIMIT 2;
SELECT * FROM flights ORDER BY duration ASC;  -- ASC = ASCENDING
SELECT * FROM flights ORDER BY duration DESC; -- DESC = DESCENDING
SELECT * FROM flights ORDER BY duration ASC LIMIT 3;
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
SELECT * FROM flights WHERE origin = 'Moscow' OR duration > 450 ORDER BY duration ASC;
SELECT * FROM flights ORDER BY id ASC;
SELECT * FROM flights WHERE id = 1;

-- for passengers TABLE
SELECT * FROM passengers;
SELECT * FROM passengers WHERE name = 'Alice';
SELECT * FROM passengers WHERE flight_id = 2;
SELECT flight_id, COUNT(*) FROM passengers GROUP BY flight_id; 