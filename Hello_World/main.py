import PyQt5
import sys , os
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label_widget = QLabel("Hello World!")

        layout.addWidget(label_widget)

        self.setLayout(layout)

        self.show


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())