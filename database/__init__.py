###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

import sqlite3
from pathlib import Path
import bcrypt

DB_PATH = Path(__file__).parent / 'app.db'

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def add_user(username, hashed_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def can_login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user is None:
        conn.close()
        return False

    stored_password = user[2]

    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        conn.close()
        return True

    conn.close()
    return False

# sql = """CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL
# );"""
# cursor.execute(sql)
# password = 'password123'
# cursor.execute('INSERT INTO users (id, username, password) VALUES (?, ?, ?)', (0, 'admin', bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')))
# connection.commit()
#
# cursor.execute('SELECT * FROM users')
# for row in cursor.fetchall():
#     print(row)
