-- Converts the hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Select hbtn_0c_0 database
USE hbtn_0c_0

-- Converts the first_table table to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
