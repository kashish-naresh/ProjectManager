import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from create_new_db import create_new_db
from tab_widget import TaskProjectTabs

class ToDoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To Do List")
        self.setMinimumHeight(300)

        self.central_widget = TaskProjectTabs()
        self.setCentralWidget(self.central_widget)

        self.central_widget.task_exit_button.clicked.connect(self.close)
        self.central_widget.project_exit_button.clicked.connect(self.close)

if __name__ == "__main__":
    
    if not os.path.exists("to_do.db"):
        print("Creating new database...")
        create_new_db("to_do.db")

        app = QApplication(sys.argv)
        msg = QMessageBox()
        msg.setWindowTitle("New Database")
        msg.setText("New database created")
        msg.exec_()
    else:
        
        create_new_db("to_do.db")

    app = QApplication(sys.argv)
    window = ToDoWindow()
    window.show()
    sys.exit(app.exec_())
