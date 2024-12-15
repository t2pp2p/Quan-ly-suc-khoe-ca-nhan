###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

import sqlite3
from contextlib import closing
from pathlib import Path
import bcrypt

DB_PATH = Path(__file__).parent / 'app.db'

def get_db_connection():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Cơ sở dữ liệu không tồn tại: {DB_PATH}")
    return closing(sqlite3.connect(DB_PATH))

def add_user(username, hashed_password):
    with get_db_connection() as conn:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()

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

def get_user_info(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Truy vấn thông tin người dùng (trừ password và active)
    cursor.execute('''
        SELECT id, username, ten, email, gioi_tinh
        FROM users
        WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()
    conn.close()

    # Trả về thông tin nếu tồn tại, hoặc None nếu không tìm thấy
    if user:
        return user[0], user[1], user[2], user[3], user[4]
    else:
        return None

def change_password(username, password):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cursor.execute('UPDATE users SET password = ? WHERE username = ?', (hashed_password, username))
        conn.commit()


def change_email(username, email):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET email = ? WHERE username = ?', (email, username))
        conn.commit()

def get_record_for_date(user_id, date):
    """Lấy bản ghi của người dùng cho một ngày cụ thể."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM user_metrics
        WHERE user_id = ? AND date = ?;
        ''', (user_id, date))
        record = cursor.fetchone()
        if record:
            return record
        else:
            return None  # Không tìm thấy bản ghi cho ngày này

def update_basic_metrics(user_id, date, height=None, weight=None, waist=None, sleep_time=None):
    """Cập nhật các chỉ số cơ bản: chiều cao, cân nặng, vòng eo, số giờ ngủ."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Kiểm tra nếu đã có bản ghi thỏa mãn
        cursor.execute('''
        SELECT 1 FROM user_metrics WHERE user_id = ? AND date = ?
        ''', (user_id, date))
        result = cursor.fetchone()

        if result is None:
            # Nếu không có bản ghi, tạo một bản ghi mới
            cursor.execute('''
            INSERT INTO user_metrics (user_id, date, height, weight, waist, sleep_time, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (user_id, date, height, weight, waist, sleep_time))
        else:
            # Nếu có bản ghi, chỉ cập nhật các cột cần thiết
            cursor.execute('''
            UPDATE user_metrics
            SET height = COALESCE(?, height),
                weight = COALESCE(?, weight),
                waist = COALESCE(?, waist),
                sleep_time = COALESCE(?, sleep_time),
                updated_at = CURRENT_TIMESTAMP
            WHERE user_id = ? AND date = ?
            ''', (height, weight, waist, sleep_time, user_id, date))

        conn.commit()


def update_advance_metrics(user_id, date, cholesterol=None, calories=None, resting_heart_rate=None,
                           blood_pressure=None):
    """Cập nhật các chỉ số nâng cao: cholesterol, calories, nhịp tim khi nghỉ, huyết áp."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Kiểm tra nếu đã có bản ghi thỏa mãn
        cursor.execute('''
        SELECT 1 FROM user_metrics WHERE user_id = ? AND date = ?
        ''', (user_id, date))
        result = cursor.fetchone()

        if result is None:
            # Nếu không có bản ghi, tạo một bản ghi mới
            cursor.execute('''
            INSERT INTO user_metrics (user_id, date, cholesterol, calories, resting_heart_rate, blood_pressure, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (user_id, date, cholesterol, calories, resting_heart_rate, blood_pressure))
        else:
            # Nếu có bản ghi, chỉ cập nhật các cột cần thiết
            cursor.execute('''
            UPDATE user_metrics
            SET cholesterol = COALESCE(?, cholesterol),
                calories = COALESCE(?, calories),
                resting_heart_rate = COALESCE(?, resting_heart_rate),
                blood_pressure = COALESCE(?, blood_pressure),
                updated_at = CURRENT_TIMESTAMP
            WHERE user_id = ? AND date = ?
            ''', (cholesterol, calories, resting_heart_rate, blood_pressure, user_id, date))

        conn.commit()

