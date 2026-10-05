import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# calls on the database
def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("db_name"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password"),
        host=os.getenv("db_host"),
        port=os.getenv("db_port")
    )
# stores each users details in the database
def create_user(username, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id", (username, email) 
    )
    user_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return user_id

# Stores users conversations in the database
def start_conversation(user_id):
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

# saves users conversation in the database
def save_message(conversation_id, sender, message):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (conversation_id, sender, message) VALUES (%s, %s, %s)", 
        (conversation_id, sender, message)
    )
    conn.commit()
    cur.close()
    conn.close()

# This gets messages stored about specific users
def get_message(conversation_id):
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

# this gets unique usernames from the users table
def get_user_by_username(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM users WHERE username = %s", (username,)
    
    )
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result



    