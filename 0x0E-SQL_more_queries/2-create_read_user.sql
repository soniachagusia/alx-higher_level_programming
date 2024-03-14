-- Script that Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- If user does not exist create it
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Use flush to apply the prividlege changes
FLUSH PRIVILEGES;
