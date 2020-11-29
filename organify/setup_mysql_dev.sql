CREATE DATABASE IF NOT EXISTS cal_win_db;
CREATE USER IF NOT EXISTS 'cal_dev'@'localhost' IDENTIFIED BY 'cal_dev_pwd';
GRANT ALL PRIVILEGES ON cal_win_db.* TO 'cal_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'cal_dev'@'localhost';
