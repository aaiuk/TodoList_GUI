import sys
from PyQt6.QtWidgets import(QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QComboBox)

class Task:
    def __init__(self, name, category, due_date, repeat_days, subtasks=None):
        self.name = name
        self.category = category
        self.due_date = due_date
        self.repeat_days = repeat_days
        self.subtasks = subtasks if subtasks else []

    def __str__(self):
        return f"{self.name} - Due: {str(self.due_date)}"

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        
        a = Task(name="test", category="Work", due_date="2024/04/16", repeat_days="Monday", subtasks=None)
        self.tasks = [a]
        self.categories = ["Work", "Personal", "Hobby"]
        

        self.layout = QVBoxLayout()
        self.category_filter = QComboBox()
        self.category_filter.addItems(["All"] + self.categories)
        self.category_filter.currentIndexChanged.connect(self.refresh_task_list)
       
        self.task_list = QListWidget()
        for task in self.tasks:
            item = QListWidgetItem(str(task))
            self.task_list.addItem(item)
        
        self.layout.addWidget(self.category_filter)
        self.layout.addWidget(self.task_list)

        self.setLayout(self.layout)

    def refresh_task_list(self):
        self.task_list.clear()
        selected_category = self.category_filter.currentText()
        for task in self.tasks:
            if selected_category == "All" or task.category == selected_category:
                item = QListWidgetItem(str(task))
                self.task_list.addItem(item)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.showMaximized()
    sys.exit(app.exec())