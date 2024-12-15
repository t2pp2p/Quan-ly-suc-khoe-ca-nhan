from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

class HeightDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Cập nhật chiều cao")
        self.setFixedSize(300, 150)

        # Giá trị chiều cao hợp lệ
        self.valid_height = None

        # Layout chính
        layout = QVBoxLayout()

        # Thông báo nhắc nhở
        self.label = QLabel("Chiều cao là chỉ số chậm thay đổi, cân nhắc khi cập nhật.")
        self.label.setWordWrap(True)
        layout.addWidget(self.label)

        # Input nhập chiều cao
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Nhập chiều cao (cm)")
        self.height_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.height_input)

        # Nút Xác nhận
        self.confirm_button = QPushButton("Xác nhận")
        self.confirm_button.clicked.connect(self.validate_height)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def validate_height(self):
        height_text = self.height_input.text().strip()
        try:
            # Kiểm tra giá trị nhập vào có hợp lệ hay không
            height = float(height_text)
            if height <= 0 or height > 300:
                raise ValueError("Chiều cao phải nằm trong khoảng hợp lý (0 - 300 cm).")

            self.valid_height = height
            QMessageBox.information(self, "Thành công", f"Chiều cao đã được cập nhật: {height} cm")
            self.accept()  # Đóng dialog khi xác nhận thành công

        except ValueError as e:
            QMessageBox.warning(self, "Lỗi", str(e))
        except Exception:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập một số hợp lệ.")