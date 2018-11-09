CREATE TABLE Crimes
(
  longitude DOUBLE PRECISION NOT NULL,
  latitude DOUBLE PRECISION NOT NULL,
  id NUMERIC(10) NOT NULL PRIMARY KEY,
  date_occu DATE,
  time_occu TIME,
  time_stamp TIMESTAMP,
  description TEXT,
  type TEXT
);

CREATE TABLE Districts
(
  id NUMERIC(10) NOT NULL PRIMARY KEY,
  beat_num NUMERIC(10) NOT NULL,
  contiguous BOOLEAN,
  district TEXT
);

CREATE TABLE Location
(
  inci_id NUMERIC(10) REFERENCES Crimes(id),
  dist_id NUMERIC(10) NOT NULL
);
