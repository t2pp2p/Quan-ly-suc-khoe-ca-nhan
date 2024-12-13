import matplotlib.pyplot as plt
import numpy as np

# Thiết kế dữ liệu giả lập
time_period = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']

# Các chỉ số
height = [170] * 7  # Chiều cao cố định (cm)
weight = [65, 65.2, 65.1, 64.9, 65, 64.8, 64.7]  # Cân nặng (kg)
waist = [80, 79.8, 79.7, 79.6, 79.5, 79.4, 79.3]  # Vòng eo (cm)
blood_pressure = [(120, 80), (122, 82), (121, 81), (119, 79), (118, 78), (120, 80), (121, 79)]  # Huyết áp (mmHg)
calories = [2000, 2100, 1900, 1950, 2050, 2000, 1980]  # Calo tiêu thụ (kcal)
cholesterol = [180, 185, 175, 170, 190, 180, 178]  # Cholesterol (mg/dL)
resting_heart_rate = [70, 72, 71, 69, 70, 68, 69]  # Nhịp tim khi nghỉ (bpm)
sleep_time = [7.5, 8, 6.5, 7, 7.8, 8, 7.2]  # Thời gian ngủ (giờ)

# Tạo biểu đồ
fig, axs = plt.subplots(4, 2, figsize=(15, 20))
fig.suptitle('Biểu đồ các chỉ số sức khỏe theo thời gian', fontsize=16)

# 1. Chiều cao
axs[0, 0].plot(time_period, height, marker='o', color='purple')
axs[0, 0].set_title('Chiều cao (cm)')
axs[0, 0].set_ylabel('Chiều cao (cm)')
axs[0, 0].grid(True)

# 2. Cân nặng
axs[0, 1].plot(time_period, weight, marker='o', color='pink')
axs[0, 1].set_title('Cân nặng (kg)')
axs[0, 1].set_ylabel('Cân nặng (kg)')
axs[0, 1].grid(True)

# 3. Vòng eo
axs[1, 0].plot(time_period, waist, marker='o', color='green')
axs[1, 0].set_title('Vòng eo (cm)')
axs[1, 0].set_ylabel('Vòng eo (cm)')
axs[1, 0].grid(True)

# 4. Huyết áp
systolic = [bp[0] for bp in blood_pressure]
diastolic = [bp[1] for bp in blood_pressure]
axs[1, 1].plot(time_period, systolic, marker='o', label='Tâm thu', color='blue')
axs[1, 1].plot(time_period, diastolic, marker='o', label='Tâm trương', color='cyan')
axs[1, 1].set_title('Huyết áp (mmHg)')
axs[1, 1].set_ylabel('mmHg')
axs[1, 1].legend()
axs[1, 1].grid(True)

# 5. Calo tiêu thụ
axs[2, 0].bar(time_period, calories, color='orange')
axs[2, 0].set_title('Calo tiêu thụ (kcal)')
axs[2, 0].set_ylabel('Calo (kcal)')
axs[2, 0].grid(True)

# 6. Cholesterol tiêu thụ
axs[2, 1].plot(time_period, cholesterol, marker='o', color='red')
axs[2, 1].set_title('Cholesterol tiêu thụ (mg/dL)')
axs[2, 1].set_ylabel('Cholesterol (mg/dL)')
axs[2, 1].grid(True)

# 7. Nhịp tim khi nghỉ
axs[3, 0].plot(time_period, resting_heart_rate, marker='o', color='brown')
axs[3, 0].set_title('Nhịp tim khi nghỉ (bpm)')
axs[3, 0].set_ylabel('Nhịp tim (bpm)')
axs[3, 0].grid(True)

# 8. Thời gian ngủ
axs[3, 1].bar(time_period, sleep_time, color='teal')
axs[3, 1].set_title('Thời gian ngủ (giờ)')
axs[3, 1].set_ylabel('Thời gian (giờ)')
axs[3, 1].grid(True)

# Hiển thị biểu đồ
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
