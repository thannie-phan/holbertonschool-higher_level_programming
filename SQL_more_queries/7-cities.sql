-- creates table database hbtn_0d_usa and table cities (in the database hbtn_0d_usa)
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table


CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);