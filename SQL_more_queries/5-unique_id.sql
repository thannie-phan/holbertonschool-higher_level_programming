-- creates table unique_id with id INT with default value 1 and must be unique and name VARCHAR(256)


CREATE TABLE IF NOT EXISTS unique_id(
    id INT PRIMARY KEY DEFAULT 1,
    name VARCHAR(256)
);