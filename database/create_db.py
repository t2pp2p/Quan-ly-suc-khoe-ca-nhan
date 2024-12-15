import sqlite3
from pathlib import Path

###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

DB_PATH = Path(__file__).parent / 'app.db'

def create_users_table():
    # Kết nối đến database SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tạo bảng users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            ten TEXT DEFAULT NULL,
            email TEXT DEFAULT NULL,
            gioi_tinh TEXT CHECK(gioi_tinh IN ('Nam', 'Nu', 'Khac')) DEFAULT NULL,
            active INTEGER CHECK(active IN (0, 1)) DEFAULT 1
        )
    ''')

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

create_users_table()

def add_admin_user(id, username, password, ten, email, gioi_tinh):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Chèn bản ghi với id đặc biệt
    try:
        cursor.execute('''
            INSERT INTO users (id, username, password, ten, email, gioi_tinh) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (id, username, password, ten, email, gioi_tinh))
        conn.commit()
        print(f"Admin với id {id} đã được thêm thành công!")
    except sqlite3.IntegrityError as e:
        print(f"Lỗi: Không thể thêm admin (có thể id {id} đã tồn tại). Chi tiết: {e}")
    finally:
        conn.close()

# Thêm tài khoản admin với id = 0
# add_admin_user(
#     id=0,
#     username='admin',
#     password='$2b$12$OVMczwc/Te79nX46dti/FOS6m2cP3OkAXVA/irt9zofq8ENx2EtEq',  # Mật khẩu mã hóa bcrypt
#     ten='Tàng Trọng Phi',
#     email='test@email.com',
#     gioi_tinh='Nam'
# )

def create_user_metrics_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,      -- ID duy nhất cho mỗi bản ghi
    user_id INTEGER NOT NULL,                  -- ID người dùng (liên kết với bảng users)
    date DATE NOT NULL,                        -- Ngày ghi nhận dữ liệu (duy nhất cho mỗi ngày)
    height REAL DEFAULT NULL,                  -- Chiều cao (cm)
    weight REAL DEFAULT NULL,                  -- Cân nặng (kg)
    waist REAL DEFAULT NULL,                   -- Vòng eo (cm)
    cholesterol REAL DEFAULT NULL,             -- Cholesterol tiêu thụ (mg)
    calories REAL DEFAULT NULL,                -- Calo tiêu thụ (kcal)
    resting_heart_rate REAL DEFAULT NULL,      -- Nhịp tim khi nghỉ (bpm)
    sleep_time REAL DEFAULT NULL,              -- Thời gian ngủ (giờ)
    blood_pressure TEXT DEFAULT NULL,          -- Huyết áp (ví dụ: '120/80')
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Thời gian cập nhật gần nhất
    UNIQUE(user_id, date),                     -- Đảm bảo mỗi người dùng chỉ có 1 bản ghi mỗi ngày
    FOREIGN KEY(user_id) REFERENCES users(id)  -- Khóa ngoại liên kết với bảng users
);
""")
    conn.commit()
    conn.close()

create_user_metrics_table()