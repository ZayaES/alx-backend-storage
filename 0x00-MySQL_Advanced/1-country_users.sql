-- about creating table users
-- CREATE DATABASE IF NOT EXISTS holberton;
-- USE holberton;

-- creates a table users
CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US'
	);
