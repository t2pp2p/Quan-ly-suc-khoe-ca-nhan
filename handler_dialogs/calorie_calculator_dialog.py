from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox)

class CalorieCalculatorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calorie Consumption Calculator")

        # Thuộc tính để lưu kết quả
        self.net_calories = None

        # Layout setup
        layout = QVBoxLayout()

        # Food type input
        self.food_label = QLabel("Select Food Type:")
        layout.addWidget(self.food_label)

        self.food_combo = QComboBox()
        self.food_combo.addItems([
            "Red Meat", "Fish", "Vegetables", "Fruits", "Grains", "Dairy Products"
        ])
        layout.addWidget(self.food_combo)

        # Steps input
        self.steps_label = QLabel("Number of Steps:")
        layout.addWidget(self.steps_label)

        self.steps_input = QLineEdit()
        self.steps_input.setPlaceholderText("Enter steps walked")
        layout.addWidget(self.steps_input)

        # Calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_calories)
        layout.addWidget(self.calculate_button)

        # OK button to close the dialog
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)  # Đóng dialog
        layout.addWidget(self.ok_button)

        # Set the layout
        self.setLayout(layout)

    def calculate_calories(self):
        try:
            # Food calories estimation (example values in kcal)
            food_calories = {
                "Red Meat": 250,
                "Fish": 200,
                "Vegetables": 50,
                "Fruits": 60,
                "Grains": 150,
                "Dairy Products": 120
            }

            food_type = self.food_combo.currentText()
            steps = self.steps_input.text()

            # Validate input
            if not steps.isdigit() or int(steps) <= 0:
                raise ValueError("Number of steps must be a positive integer greater than 0.")

            steps = int(steps)
            calories_burned = steps * 0.04  # Example: 0.04 kcal per step

            # Calculate total calories
            self.net_calories = food_calories[food_type] - calories_burned

            # Handle case where calories are negative (user consumed more than burned)
            if self.net_calories < 0:
                QMessageBox.warning(self, "Calorie Calculation",
                                    "You have burned more calories than you consumed. Please check your input.")
                return

            # Show result with units
            QMessageBox.information(self, "Calorie Calculation",
                                    f"Net Calories: {self.net_calories:.2f} kcal")

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))

    def get_result(self):
        return self.net_calories


# Function to show the dialog
def show_calorie_calculator_dialog():
    dialog = CalorieCalculatorDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        return dialog.get_result()
    return None
