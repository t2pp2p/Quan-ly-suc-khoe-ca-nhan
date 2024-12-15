from datetime import datetime
from tkinter import messagebox
from database import can_login, change_password
import re

###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

def get_current_date_time_info():
    # Lấy thời gian hiện tại
    now = datetime.now()

    # Mapping từ tên thứ tiếng Anh sang tiếng Việt
    weekday_mapping = {
        "Monday": "Thứ hai",
        "Tuesday": "Thứ ba",
        "Wednesday": "Thứ tư",
        "Thursday": "Thứ năm",
        "Friday": "Thứ sáu",
        "Saturday": "Thứ bảy",
        "Sunday": "Chủ nhật"
    }

    # Lấy tên thứ (tiếng Anh) và chuyển sang tiếng Việt
    day_of_week_english = now.strftime("%A")
    day_of_week_vn = weekday_mapping[day_of_week_english]

    # Lấy ngày, tháng, năm
    day = now.day
    month = now.month
    year = now.year

    # Lấy giờ và phút
    hour = now.hour
    minute = now.minute

    # Trả về kết quả
    return day_of_week_vn, day, month, year, hour, minute


def get_date_info_from_input(day, month, year):
    try:
        # Tạo đối tượng datetime từ đầu vào
        date = datetime(year, month, day)

        # Mapping từ tên thứ tiếng Anh sang tiếng Việt
        weekday_mapping = {
            "Monday": "Thứ hai",
            "Tuesday": "Thứ ba",
            "Wednesday": "Thứ tư",
            "Thursday": "Thứ năm",
            "Friday": "Thứ sáu",
            "Saturday": "Thứ bảy",
            "Sunday": "Chủ nhật"
        }

        # Lấy tên thứ (tiếng Anh) và chuyển sang tiếng Việt
        day_of_week_english = date.strftime("%A")
        day_of_week_vn = weekday_mapping[day_of_week_english]

        # Trả về kết quả
        return day_of_week_vn, day, month, year
    except ValueError:
        # Xử lý nếu ngày không hợp lệ
        return None, None, None, None

def can_change_password(username, old_password, new_password, confirm_password):
    if new_password != confirm_password:
        messagebox.showwarning("", "Mật khẩu và xác nhận mật khẩu không đúng!")
        return
    if not can_login(username, old_password):
        messagebox.showwarning("","Mật khẩu hiện tại chưa đúng!")
        return
    messagebox.showinfo("", "Mật khẩu đã thay đổi!")
    change_password(username, new_password)

def validate_basic_metrics(height_cm: str, weight_kg: str, waist_cm: str, sleep_hours: str):
    """
    Validate and parse basic health metrics: height (cm), weight (kg), waist (cm), sleep hours (hours).

    :param height_cm: Height in centimeters (string input).
    :param weight_kg: Weight in kilograms (string input).
    :param waist_cm: Waist circumference in centimeters (string input).
    :param sleep_hours: Sleep hours per night (string input).
    :return: A dictionary with validated and parsed metrics.
    """
    try:
        height = float(height_cm)
        if height <= 0 or height > 300:
            raise ValueError("Height must be a positive value less than or equal to 300 cm.")

        weight = float(weight_kg)
        if weight <= 0 or weight > 500:
            raise ValueError("Weight must be a positive value less than or equal to 500 kg.")

        waist = float(waist_cm)
        if waist <= 0 or waist > 200:
            raise ValueError("Waist circumference must be a positive value less than or equal to 200 cm.")

        sleep = float(sleep_hours)
        if sleep < 0 or sleep > 24:
            raise ValueError("Sleep hours must be between 0 and 24 hours.")

        return {
            "height_cm": height,
            "weight_kg": weight,
            "waist_cm": waist,
            "sleep_hours": sleep
        }
    except ValueError as e:
        return {"error": str(e)}


def validate_and_parse_float(value: str, min_value: float, max_value: float, field_name: str) -> float:
    value = value.strip()  # Loại bỏ khoảng trắng thừa
    if value == "":  # Kiểm tra chuỗi trống
        raise ValueError(f"{field_name} cannot be empty.")

    try:
        value = float(value)
        if value < min_value or value > max_value:
            raise ValueError(f"{field_name} must be between {min_value} and {max_value}.")
        return value
    except ValueError:
        raise ValueError(f"{field_name} must be a valid number.")


def validate_and_parse_int(value: str, min_value: int, max_value: int, field_name: str) -> int:
    value = value.strip()  # Loại bỏ khoảng trắng thừa
    if value == "":  # Kiểm tra chuỗi trống
        raise ValueError(f"{field_name} cannot be empty.")

    try:
        value = int(value)
        if value < min_value or value > max_value:
            raise ValueError(f"{field_name} must be between {min_value} and {max_value}.")
        return value
    except ValueError:
        raise ValueError(f"{field_name} must be a valid integer.")


def validate_blood_pressure(value: str) -> dict:
    value = value.strip()  # Loại bỏ khoảng trắng thừa
    if not re.match(r"^\d{2,3}/\d{2,3}$", value):
        raise ValueError("Blood pressure must be in the format 'SYS/DIA', e.g., '120/80'.")

    sys, dia = map(int, value.split("/"))
    if sys < 50 or sys > 250 or dia < 30 or dia > 150:
        raise ValueError(
            "Systolic pressure must be between 50-250 mmHg and diastolic pressure must be between 30-150 mmHg.")

    return {"systolic": sys, "diastolic": dia}


def validate_advance_metrics(cholesterol_mg: str, calories_kcal: str, resting_heart_rate: str, blood_pressure: str):
    try:
        # Validate and parse cholesterol
        cholesterol = validate_and_parse_float(cholesterol_mg, 0, 10000, "Cholesterol")

        # Validate and parse calories
        calories = validate_and_parse_float(calories_kcal, 0, 20000, "Calories")

        # Validate and parse heart rate
        heart_rate = validate_and_parse_int(resting_heart_rate, 1, 300, "Resting heart rate")

        # Validate and parse blood pressure
        blood_pressure_data = validate_blood_pressure(blood_pressure)

        return {
            "cholesterol_mg": cholesterol,
            "calories_kcal": calories,
            "resting_heart_rate_bpm": heart_rate,
            "blood_pressure": blood_pressure_data
        }

    except ValueError as e:
        return {"error": str(e)}

def chuyen_doi_ngay(chuoi):
    # Biểu thức chính quy để trích xuất ngày, tháng, năm
    pattern = r"ngày (\d{1,2}) tháng (\d{1,2}) năm (\d{4})"
    match = re.search(pattern, chuoi)

    if match:
        # Lấy các nhóm (day, month, year)
        day, month, year = match.groups()
        # Định dạng thành 'yyyy-mm-dd'
        return f"{year}-{int(month):02d}-{int(day):02d}"
    else:
        return "Không tìm thấy ngày tháng năm trong chuỗi!"