import sys
from PyQt6.QtWidgets import(QApplication, QWidget)

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())