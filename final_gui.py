from time import sleep
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class LED(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('LED')
        self.setGeometry(100, 100, 200, 200)

        layout = QVBoxLayout()

        self.label = QLabel("")
        layout.addWidget(self.label)

        self.setLayout(layout)

    def update_led(self, P):
        if P > -5:
            self.label.setStyleSheet("background-color: green")
            self.label.setText("LED: ON")
        else:
            self.label.setStyleSheet("background-color: red")
            self.label.setText("LED: OFF")
