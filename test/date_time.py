import re

# Chuỗi đầu vào
chuoi = "Thứ bảy, ngày 15 tháng 12 năm 2024"

# Biểu thức chính quy để trích xuất ngày, tháng, năm
pattern = r"ngày (\d{1,2}) tháng (\d{1,2}) năm (\d{4})"

# Tìm kiếm với biểu thức chính quy
match = re.search(pattern, chuoi)

if match:
    # Lấy các nhóm (day, month, year)
    day, month, year = match.groups()
    # Chuyển thành định dạng YYYY-MM-DD
    ngay_thang_nam = f"{year}-{int(month):02d}-{int(day):02d}"
    print(ngay_thang_nam)
else:
    print("Không tìm thấy ngày tháng năm trong chuỗi!")
