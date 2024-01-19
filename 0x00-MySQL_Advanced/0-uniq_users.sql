-- creates a table user --

---creates a table named user ---
CREATE TABLE IF NOT EXISTS `users` (
	id INT IDENTITY(1,1) PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);
