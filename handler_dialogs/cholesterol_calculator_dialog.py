from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox)


class CholesterolCalculatorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cholesterol Consumption Calculator")

        # Thuộc tính để lưu kết quả
        self.net_cholesterol = None

        # Layout setup
        layout = QVBoxLayout()

        # Food type input
        self.food_label = QLabel("Select Food Type:")
        layout.addWidget(self.food_label)

        self.food_combo = QComboBox()
        self.food_combo.addItems([
            "Eggs", "Red Meat", "Fish", "Dairy Products", "Vegetables", "Fruits"
        ])
        layout.addWidget(self.food_combo)

        # Tooltip cho combo box
        self.food_combo.setToolTip("Select the type of food to calculate cholesterol.")

        # Quantity input
        self.quantity_label = QLabel("Quantity (grams):")
        layout.addWidget(self.quantity_label)

        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Enter quantity in grams")
        layout.addWidget(self.quantity_input)

        # Tooltip cho input số lượng
        self.quantity_input.setToolTip("Enter the quantity of food in grams.")

        # Calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_cholesterol)
        layout.addWidget(self.calculate_button)

        # OK button to close the dialog
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)  # Đóng dialog
        layout.addWidget(self.ok_button)

        # Set the layout
        self.setLayout(layout)

    def calculate_cholesterol(self):
        try:
            # Cholesterol estimation (example values in mg per 100g)
            cholesterol_content = {
                "Eggs": 373,
                "Red Meat": 88,
                "Fish": 55,
                "Dairy Products": 50,
                "Vegetables": 0,
                "Fruits": 0
            }

            food_type = self.food_combo.currentText()
            quantity = self.quantity_input.text()

            # Validate input
            if not quantity.isdigit():
                raise ValueError("Quantity must be a positive integer.")

            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

            # Calculate cholesterol
            cholesterol = (cholesterol_content[food_type] * quantity) / 100

            # Save result
            self.net_cholesterol = cholesterol

            # Show result
            QMessageBox.information(self, "Cholesterol Calculation",
                                    f"Net Cholesterol: {self.net_cholesterol:.2f} mg")

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))

    def get_result(self):
        return self.net_cholesterol


# Function to show the dialog
def show_cholesterol_calculator_dialog():
    dialog = CholesterolCalculatorDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        return dialog.get_result()
    return None
