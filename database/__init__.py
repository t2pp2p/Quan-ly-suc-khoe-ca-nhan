###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

import sqlite3
from contextlib import closing
from pathlib import Path
import bcrypt

DB_PATH = Path(__file__).parent / 'app.db'

# def get_db_connection():
#     # Tạo cơ sở dữ liệu nếu chưa tồn tại, việc này tùy biến
#     if not DB_PATH.exists():
#         with closing(sqlite3.connect(DB_PATH)) as conn:
#             # Có thể tạo các bảng cơ bản hoặc thực hiện một số thao tác chuẩn bị
#             cursor = conn.cursor()
#             # Ví dụ: Tạo bảng mặc định
#             cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     username TEXT NOT NULL,
#                     password TEXT NOT NULL
#                 )
#             ''')
#             conn.commit()
#
#     # Trả về kết nối cơ sở dữ liệu
#     return closing(sqlite3.connect(DB_PATH))
def get_db_connection():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Cơ sở dữ liệu không tồn tại: {DB_PATH}")
    return closing(sqlite3.connect(DB_PATH))

def add_user(username, hashed_password):
    with get_db_connection() as conn:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

def can_login(username, password):
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
            return True
    return False

def exist_user(username):
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT 1 FROM users WHERE username = ?', (username,))
        return cursor.fetchone() is not None

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
