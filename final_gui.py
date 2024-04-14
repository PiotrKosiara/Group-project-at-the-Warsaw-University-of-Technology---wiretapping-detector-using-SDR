import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from time import sleep

class DiodyBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 400)
        self.P = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        bar_width = 20
        bar_height = self.height()
        step = bar_height / 20

        for i in range(20):
            transparency = min(255, max(0, int((self.P - i) * 255 / 20)))
            color = QColor(i*12, 255-i*12, 0, transparency)
            painter.setBrush(color)
            painter.drawRect(0, bar_height - (i + 1) * step, bar_width, step)

    def set_P(self, P):
        self.P = P
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diody Bar")
        self.setGeometry(100, 100, 250, 450)

        self.diody_bar = DiodyBar(self)
        self.setCentralWidget(self.diody_bar)

        self.label = QLabel("P: 0", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 400, 250, 50)

    def update_led(self, value):
        self.diody_bar.set_P(value)
        self.label.setText("P: {:.2f}".format(value))

# def xd(nums):
#     for num in nums:
#         window.update_led(num)
#         QApplication.processEvents()
#         sleep(2)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#
#     nums = [10, 200, 30, 10, 200, 30, 100, 30, 100, 20, 20, 200, 0, 255, 30]
#     xd(nums)
#
#     sys.exit(app.exec_())