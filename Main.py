from Input import INPUT
from Result import RESULT
from Steps import STEPS

from PyQt5.QtWidgets import QApplication

class UI():
    def __init__(self):
        self.input = INPUT()
        self.input.show()
        self.input.btn_Ok.clicked.connect(self.Load_Data)

        self.result = RESULT()
        self.result.btn_Result.clicked.connect(self.Detailed_Steps)

        self.steps = STEPS()
        self.steps.btn_Complete.clicked.connect(self.Result_Page)

    def Load_Data(self):
        self.result.start_state = [
            [self.input.start_00.text(), self.input.start_01.text(), self.input.start_02.text()],
            [self.input.start_10.text(), self.input.start_11.text(), self.input.start_12.text()],
            [self.input.start_20.text(), self.input.start_21.text(), self.input.start_22.text()]
        ]

        self.result.destination_state = [
            [self.input.goal_00.text(), self.input.goal_01.text(), self.input.goal_02.text()],
            [self.input.goal_10.text(), self.input.goal_11.text(), self.input.goal_12.text()],
            [self.input.goal_20.text(), self.input.goal_21.text(), self.input.goal_22.text()]
        ]

        for i in range(3):
            for j in range(3):
                getattr(self.result, f"cur_{i}{j}").setText(self.result.start_state[i][j])

        self.input.hide()
        self.result.show()

    def Detailed_Steps(self):
        self.steps.result = self.result.result
        self.result.hide()
        self.steps.show()
        self.steps.load_result_to_table()

    def Result_Page(self):
        self.steps.hide()
        self.result.show()


if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    app.exec_()
