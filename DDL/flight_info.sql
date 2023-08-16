CREATE TABLE flightapp.flight_details (
	id VARCHAR[100] PRIMARY KEY,
	departure_time TIME,
	arrival_time TIME,
	duration TEXT,
	departure_airport_code CHAR, 
	arrival_airport_code CHAR,
	airline_codes TEXT,
	stopover_airport_codes TEXT,
	alliance_codes TEXT,
	stopovers_count INTEGER,
	departure_datetime TIMESTAMP,
	arrival_datetime TIMESTAMP,
	stopover_duration_min INTEGER,
	duration_min INTEGER,
	overnight BOOLEAN,
	stopover_duration TEXT,
	duration_days INTEGER,
	longstopover BOOLEAN
	);
	