COPY crimes
FROM '/home/harry/github/National_Crime_Map/database/data/durham_2018_crime.csv' DELIMITER ',' CSV HEADER;

COPY districts
FROM '/home/harry/github/National_Crime_Map/database/data/durham_2018_districts.csv' DELIMITER ',' CSV HEADER;

COPY location
FROM '/home/harry/github/National_Crime_Map/database/data/durham_2018_dc.csv' DELIMITER ',' CSV HEADER;
