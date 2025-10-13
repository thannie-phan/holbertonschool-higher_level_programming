-- creates a table called first_table
-- id INT and -- name VARCHAR(256)
-- if table alr exists, script should not fail

CREATE TABLE IF NOT EXISTS first_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);