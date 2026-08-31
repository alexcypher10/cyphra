import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("db_name"),
    user=os.getenv("db_user"),
    password=os.getenv("db_password"),
    host=os.getenv("db_host"),
    port=os.getenv("db_port")
)
cur = conn.cursor()
cur.execute("SELECT * FROM users; ")
results = cur.fetchall()
print(results)

cur.execute("INSERT INTO users (username, email) VALUES (%s, %s)", ("user1", "cypher@gmail.com"))
conn.commit()
cur.close
conn.close()

