-- Crime Count --
SELECT COUNT(*)
FROM crimes
WHERE AGE(time_stamp) < INTERVAL '90 days';

-- Type1 Crime --
SELECT COUNT(*)
FROM crimes
WHERE LOWER(description) || LOWER(type) LIKE ANY(ARRAY['%aggravated assault%',
  '%larceny%', '%break in%', '%rape%', '%robbery%', '%robb%', '%carjack%',
  '%arson%', '%stolen vehicle%', '%stabbing%', '%abduction%', '%kidnap%',
  '%home invasion%', '%hostage%', '%murder%', '%homicide%', '%manslaughter%']);

-- Murder --
SELECT COUNT(*)
FROM crimes
WHERE LOWER(description) || LOWER(type) LIKE ANY(ARRAY['%murder%', '%homicide%', '%manslaughter%']);

-- Robbery --
SELECT COUNT(*)
FROM crimes
WHERE LOWER(description) || LOWER(type) LIKE ANY(ARRAY['%robbery%', '%robb%', '%carjack%']);

-- Assault --
SELECT COUNT(*)
FROM crimes
WHERE LOWER(description) || LOWER(type) LIKE ANY(ARRAY['%aggravated assault%', '%kidnap%', '%abduction%', '%stabbing%']);

-- Rape --
SELECT COUNT(*)
FROM crimes
WHERE LOWER(description) || LOWER(type) LIKE ANY(ARRAY['%rape%']);

-- by region --
SELECT COUNT(*)
FROM crimes, location
WHERE location.inci_id = crimes.id
AND location.dist_id = 0
AND LOWER(description) || LOWER(type) LIKE ANY(ARRAY['%rape%']);
