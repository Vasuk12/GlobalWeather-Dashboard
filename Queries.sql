-- CREATE TABLE weather_data (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     country VARCHAR(100),
--     location_name VARCHAR(255),
--     latitude DECIMAL(9, 6),
--     longitude DECIMAL(9, 6),
--     timezone VARCHAR(50),
--     last_updated_epoch INT,
--     last_updated DATETIME,
--     temperature_celsius FLOAT,
--     temperature_fahrenheit FLOAT,
--     condition_text VARCHAR(50),
--     wind_mph FLOAT,
--     wind_kph FLOAT,
--     wind_degree INT,
--     wind_direction VARCHAR(5),
--     pressure_mb FLOAT,
--     pressure_in FLOAT,
--     precip_mm FLOAT,
--     precip_in FLOAT,
--     humidity INT,
--     cloud INT,
--     feels_like_celsius FLOAT,
--     feels_like_fahrenheit FLOAT,
--     visibility_km FLOAT,
--     visibility_miles FLOAT,
--     uv_index FLOAT,
--     gust_mph FLOAT,
--     gust_kph FLOAT,
--     air_quality_Carbon_Monoxide FLOAT,
--     air_quality_Ozone FLOAT,
--     air_quality_Nitrogen_dioxide FLOAT,
--     air_quality_Sulphur_dioxide FLOAT,
--     air_quality_PM2_5 FLOAT,  -- Changed from air_quality_PM2.5
--     air_quality_PM10 FLOAT,
--     air_quality_us_epa_index VARCHAR(255),  -- Changed from air_quality_us-epa-index
--     air_quality_gb_defra_index INT,  -- Changed from air_quality_gb-defra-index
--     sunrise TIME,
--     sunset TIME,
--     moonrise TIME,
--     moonset TIME,
--     moon_phase VARCHAR(50),
--     moon_illumination INT
-- );


-- SELECT * FROM weather_data LIMIT 10;

-- LOAD DATA LOCAL INFILE '/Users/vasukhare/Applications/Full Stack Data Science Project/cleaned_weather_data.csv'
-- INTO TABLE weather_data
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"' 
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

-- ALTER TABLE `weather_data`
-- CHANGE COLUMN `air_quality_PM2.5` `air_quality_PM2_5` FLOAT;

-- ALTER TABLE `weather_data`
-- RENAME COLUMN `air_quality_PM2_5` TO `air_quality_PM2.5`;

-- ALTER TABLE `weather_data`
-- CHANGE COLUMN `air_quality_us-epa-index` `air_quality_us_epa_index` VARCHAR(255);

-- DESCRIBE weather_data;

-- SHOW COLUMNS FROM weather_data;

-- ALTER TABLE weather_data
-- CHANGE air_quality_us_epa_index `air_quality_us-epa-index` VARCHAR(255);

-- INSERT INTO `weather_data` (sunrise, sunset) VALUES
-- ('04:50:00', '18:50:00'),  -- Converted from 04:50 AM and 06:50 PM
-- ('05:21:00', '19:54:00');  -- Converted from 05:21 AM and 07:54 PM
-- SELECT * FROM weather_data;
-- SELECT * FROM weather_data;


-- SELECT COUNT(*) FROM weather_data WHERE temperature_celsius IS NULL;

-- SELECT * FROM weather_data WHERE temperature_celsius IS NULL OR humidity IS NULL;
-- DELETE FROM weather_data WHERE id IN (1, 2);
-- SELECT * FROM weather_data;
-- ALTER TABLE weather_data AUTO_INCREMENT = 1;

-- ALTER TABLE weather_data AUTO_INCREMENT = 1;
-- SELECT * FROM weather_data;
-- 

-- ALTER TABLE weather_data
-- CHANGE air_quality_gb_defra_index
--  `air_quality_gb-defra-index` VARCHAR(255);

-- ALTER TABLE weather_data DROP PRIMARY KEY;
-- DROP TABLE IF EXISTS weather_data;


-- Retrieve the top 5 with the lowest temprature
SELECT country, location_name, temperature_celsius, temperature_fahrenheit
FROM `weather_data`
ORDER BY temperature_celsius DESC, temperature_fahrenheit DESC
LIMIT 5;





-- Retrieve the top 5 locations with the lowest precipitation:
SELECT location_name, precip_mm, precip_in
FROM `weather_data`
ORDER BY precip_in, precip_mm ASC
LIMIT 5;

-- Retrieve All Records for a Specific Date or Condition
SELECT *
FROM `weather_data`
WHERE  timezone = 'Asia/Bangkok';

-- Retrieve Records Where Temperature > 35°C or Precipitation > 100 mm
SELECT *
FROM `weather_data`
WHERE temperature_celsius > 35 or precip_mm > 100;

-- Perform a group by operation average temperature by country
SELECT country, AVG(temperature_celsius) AS average_temperature_celsius
FROM `weather_data`
GROUP BY country;

-- Perform a group by operation total precipitation by region

SELECT location_name, SUM(precip_mm) AS total_precipitation_mm
FROM `weather_data`
GROUP BY location_name;
