from PyQt5.QtWidgets import QApplication, QFrame, QTableWidgetItem
from GUI.StepsForm import Ui_Frame

class STEPS(QFrame, Ui_Frame):
    result = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nguyễn Văn Kế - 23110234")

    def load_result_to_table(self):       
        if not self.result or len(self.result) == 0:
            print("No data available for table!")
            self.txt_Steps.setText("No data available!")
            return
        
        # Nếu muốn hiển thị dưới dạng văn bản
        formatted_text = "\n\n".join(["Step {}:\n{}".format(i, '\n'.join(map(str, step))) for i, step in enumerate(self.result)])

        # Đưa vào QTextEdit
        self.txt_Steps.setText(formatted_text)  

