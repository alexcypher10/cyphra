SELECT * FROM users;
SELECT * FROM conversations;
SELECT username, email, password_hash From users WHERE username = 'testuser';
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	email VARCHAR(255)UNIQUE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE conversations(
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users(id),
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE messages(
	id SERIAL PRIMARY KEY,
	conversation_id INTEGER REFERENCES conversations(id),
	sender VARCHAR(20) NOT NULL,
	message TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMES
	
);
DELETE FROM users;
SELECT username, verification_code, code_expires_at, is_verified FROM users WHERE username = 'cypher';

ALTER TABLE users ALTER COLUMN code_expires_at TYPE TIMESTAMP(0);