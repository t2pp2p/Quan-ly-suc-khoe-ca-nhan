from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

class EmailDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nhập Email")
        self.setGeometry(300, 300, 400, 150)

        # Label
        self.label = QLabel("Nhập địa chỉ email:")

        # Ô nhập email
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("example@example.com")

        # Validator cho ô nhập email
        email_regex = QRegularExpression(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        validator = QRegularExpressionValidator(email_regex)
        self.email_input.setValidator(validator)

        # Nút OK và Cancel
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

    def get_email(self):
        """Trả về email được nhập"""
        return self.email_input.text()
