from PyQt6.QtWidgets import QDialog, QVBoxLayout, QCalendarWidget, QPushButton
from PyQt6.QtCore import QDate

###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

class DateSelector(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chọn Ngày")
        self.setGeometry(300, 300, 400, 300)

        # Layout chính
        layout = QVBoxLayout(self)

        # Calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)  # Hiển thị lưới trong lịch
        self.calendar.setSelectedDate(QDate.currentDate())  # Ngày mặc định là hôm nay
        layout.addWidget(self.calendar)

        # Nút Xác nhận
        self.ok_button = QPushButton("Xác nhận", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

        # Nút Hủy
        self.cancel_button = QPushButton("Hủy", self)
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.cancel_button)

    def get_date(self):
        if self.exec() == QDialog.DialogCode.Accepted:
            selected_date = self.calendar.selectedDate()
            return selected_date.day(), selected_date.month(), selected_date.year()
        return None
