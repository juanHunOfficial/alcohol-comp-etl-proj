-- create the table for all the data 

CREATE TABLE IF NOT EXISTS raw_data (
    id SERIAL PRIMARY KEY,
    entity VARCHAR(255),
    code VARCHAR(255),
    year INT,
    total_alcohol_consumption_per_capita FLOAT,
    gdp_per_capita FLOAT,
    population INT,
    continent VARCHAR(255)
);

COPY raw_data (entity, code, year, total_alcohol_consumption_per_capita, gdp_per_capita, population, continent)
FROM '/data/alcohol-consumption-vs-gdp-per-capita.csv'
DELIMITER ','
CSV HEADER;