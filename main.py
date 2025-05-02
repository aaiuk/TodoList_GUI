import sys
from PyQt6.QtWidgets import(QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem)

class Task:
    def __init__(self, name, category, due_date, repeat_days, subtasks=None):
        self.name = name
        self.category = category
        self.due_date = due_date
        self.repeat_days = repeat_days
        self.subtasks = subtasks if subtasks else []

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        a = Task(name="test", category="urara", due_date="2024/04/16", repeat_days="Monday", subtasks=None)

        self.tasks = [a]

        self.layout = QVBoxLayout()
        self.task_list = QListWidget()
        self.task_list.clear()
        for task in self.tasks:
            item = QListWidgetItem(str(task))
            self.task_list.addItem(item)
        self.layout.addWidget(self.task_list)

        self.setLayout(self.layout)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.showMaximized()
    sys.exit(app.exec())