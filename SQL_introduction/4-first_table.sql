-- creates a table called first_table
-- id INT and -- name VARCHAR(256)
-- if table alr exists, script should not fail

USE hbtn_0c_0
CREATE TABLE IF NOT EXISTS first_table (
    id INT PRIMARY KEY,
    name VARCHAR(256)
);