-- creates the database hbtn_0d_2 and the user user_0d_2
-- user only SELECT privilege in the database hbtn_0d_2
-- its pw should be set to user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
