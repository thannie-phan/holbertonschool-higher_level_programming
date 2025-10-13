-- creates table database hbtn_0d_usa and table states (in the database hbtn_0d_usa)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states(
    id INT AUTO INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);