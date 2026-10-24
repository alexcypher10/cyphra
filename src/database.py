import psycopg2
from dotenv import load_dotenv
import os
import bcrypt
from email.mime.text import MIMEText

load_dotenv()

 
def get_connection():
    # calls on the database
    return psycopg2.connect(
        dbname=os.getenv("db_name"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password"),
        host=os.getenv("db_host"),                  
        port=os.getenv("db_port")
    )

def create_user(username, email, password_hash):
    # stores each users details in the database
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s) RETURNING id",
        (username, email, password_hash)
    )
    user_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return user_id


def start_conversation(user_id):
    # Stores users conversations in the database
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO conversations (user_id) VALUES (%s) RETURNING id", (user_id,)
    )
    conversation_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return conversation_id


def save_message(conversation_id, sender, message):
    # saves users conversation in the database
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (conversation_id, sender, message) VALUES (%s, %s, %s)", 
        (conversation_id, sender, message)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_message(conversation_id):
    # This gets messages stored about specific users
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT sender, message, created_at FROM messages WHERE conversation_id = %s ORDER BY created_at",
        (conversation_id,)
    )

    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results


def get_user_by_username(username):
    # this gets unique usernames from the users table
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, password_hash, verification_code, code_expires_at, is_verified  FROM users WHERE username = %s", (username,)
    
    )
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result

def mark_user_verified(user_id):
    # verifies user's code with the database
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET is_verified = TRUE, verification_code = NULL, code_expires_at = NULL WHERE id = %s ", (user_id,)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_conversation(conversation_id):
    # checks if conversation relates to user via the user id
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
       "SELECT user_id FROM conversations WHERE id = %s", (conversation_id,)
    )
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result[0] if result else None

def send_verification_code(user_id, code, expires_at):
    # sends code to the database for checking
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET verification_code = %s, code_expires_at = %s WHERE id =%s",
        (code, expires_at, user_id) )
    conn.commit()
    cur.close()
    conn.close()
    

def hash_password(password):
    # stores user password in hashed format 
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))