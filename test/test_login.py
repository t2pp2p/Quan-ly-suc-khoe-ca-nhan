import sqlite3
import bcrypt

# Kết nối cơ sở dữ liệu
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Tạo bảng (nếu chưa có)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Mã hóa mật khẩu
password = "qqqqqqqq"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Lưu vào cơ sở dữ liệu
cursor.execute('INSERT INTO users (id, username, password) VALUES (?, ?, ?)', (0, 'admin', hashed_password))
conn.commit()
conn.close()

# Kết nối cơ sở dữ liệu
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
for row in cursor:
    print(row)

# Lấy mật khẩu đã mã hóa từ cơ sở dữ liệu
username = "admin"
password_input = "qqqqqqqq"
cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
stored_password = cursor.fetchone()[0]  # Lấy giá trị mật khẩu

# Xác thực mật khẩu
if bcrypt.checkpw(password_input.encode('utf-8'), stored_password.encode('utf-8')):
    print("Mật khẩu chính xác!")
else:
    print("Mật khẩu sai!")
