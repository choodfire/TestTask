CREATE DATABASE data;

\c data;

CREATE TABLE publication (
    id SERIAL PRIMARY KEY,
    category VARCHAR(30),
    article_link VARCHAR(300),
    presskit VARCHAR(300),
    reddit_campaign VARCHAR(300),
    reddit_launch VARCHAR(300),
    reddit_media VARCHAR(300),
    reddit_recovery VARCHAR(300),
    wikipedia VARCHAR(300),
    website VARCHAR(300)
);

CREATE TABLE rocket (
    id VARCHAR(30) PRIMARY KEY,
    description TEXT,
    name VARCHAR(30),
    active BOOLEAN,
    company VARCHAR(30),
    first_flight DATE,

    publication INT,
    FOREIGN KEY (publication) REFERENCES publication (id)
);

CREATE TABLE mission (
    id VARCHAR(30) PRIMARY KEY,
    description TEXT,
    name VARCHAR(30),

    publication INT,
    FOREIGN KEY (publication) REFERENCES publication (id)
);

CREATE TABLE launch (
    id VARCHAR(30) PRIMARY KEY,
    mission_id VARCHAR(30),
    rocket_id VARCHAR(30),
    upcoming BOOLEAN,
    launch_success BOOLEAN,
    launch_date_unix DATE,

    publication INT,
    FOREIGN KEY (publication) REFERENCES publication (id),
    FOREIGN KEY (rocket_id) REFERENCES rocket (id)
);

CREATE VIEW PublicationsAmount
AS
    SELECT category, COUNT(*) as amount
    FROM publication
    where category in ('rocket', 'mission', 'launch')
    group by category