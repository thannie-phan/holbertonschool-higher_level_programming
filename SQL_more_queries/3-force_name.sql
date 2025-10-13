-- creates table force_name with id INT and name VARCHAR(256) which cannot be NULL

CREATE TABLE IF NOT EXISTS force_name(
    id INT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

