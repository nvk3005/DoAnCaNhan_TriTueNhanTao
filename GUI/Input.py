import sys
from PyQt5.QtWidgets import QApplication, QFrame
from GUI.InputForm import Ui_Frame

class INPUT(QFrame, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nguyễn Văn Kế - 23110234")

