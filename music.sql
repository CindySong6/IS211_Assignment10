CREATE TABLE artists (id INTEGER PRIMARY KEY,
name TEXT);

CREATE TABLE albums (id INTEGER PRIMARY KEY,
name TEXT,
artist_id INTEGER);

CREATE TABLE songs (id INTEGER PRIMARY KEY,
album_id INTEGER,
track_number INTEGER,
track_duration TIME )
