CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    username TEXT NOT NULL UNIQUE,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    mobile TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    hash TEXT NOT NULL);

CREATE TABLE sqlite_sequence(name,seq);

CREATE UNIQUE INDEX email ON users (email);
CREATE UNIQUE INDEX mobile ON users (mobile);
CREATE UNIQUE INDEX username ON users (username);

