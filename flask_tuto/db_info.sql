DROP TABLE IF EXISTS 'users';
DROP TABLE IF EXISTS 'posts';
		
CREATE TABLE 'users' (
  'id' INTEGER PRIMARY KEY AUTOINCREMENT,
  'username' VARCHAR(64) NOT NULL DEFAULT NULL,
  'email' VARCHAR(128) NULL DEFAULT NULL,
  'password_hash' VARCHAR(128) NOT NULL DEFAULT NULL
);

CREATE TABLE 'posts' (
  'id' INTEGER PRIMARY KEY AUTOINCREMENT,
  'body' VARCHAR(255) NOT NULL DEFAULT NULL,
  'timestamp' datetime NULL DEFAULT NULL,
  'user_id' VARCHAR(128) NOT NULL DEFAULT NULL,
  FOREIGN KEY(user_id) REFERENCES users(id)
);