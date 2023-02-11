CREATE DATABASE data;

\c data;

CREATE TABLE rocket (
    id VARCHAR(30) PRIMARY KEY,
    description TEXT,
    name VARCHAR(30),
    active BOOLEAN,
    company VARCHAR(30),
    first_flight DATE
);

CREATE TABLE launch (
    id VARCHAR(30) PRIMARY KEY,
    mission_id VARCHAR(30),
    rocket_id VARCHAR(30),
    upcoming BOOLEAN,
    launch_success BOOLEAN,
    launch_date_unix DATE,

    FOREIGN KEY (rocket_id) REFERENCES rocket (id)
);