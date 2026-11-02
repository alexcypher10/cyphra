SELECT * FROM users;
SELECT * FROM conversations;
SELECT username, email, password_hash From users WHERE username = 'testuser';
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	email VARCHAR(255)UNIQUE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	password_hash TEXT NOT NULL DEFAULT '',
	verification_code VARCHAR(6),
	code_expires_at TIMESTAMP(0),
	is_verified BOOLEAN DEFAULT FALSE
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
