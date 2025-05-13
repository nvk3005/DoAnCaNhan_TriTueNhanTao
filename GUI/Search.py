import sys
from PyQt5.QtWidgets import QApplication, QFrame
from GUI.SearchForm import Ui_Frame
from Node import Node
from tkinter import messagebox
import random
from PyQt5.QtCore import QTimer

class SEARCH(QFrame, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nguyễn Văn Kế - 23110234")
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)  # Kết nối timer với phương thức update_ui
        self.list_start_state = []
        self.list_destination_state = []
        self.result = []
        self.connection = False


    def randomize_state(self, isKnown=False):
        list_state = []
        for i in range(8):
            value = ["1", "2", "3", "4", "5", "6", "7", "8", ""]
            state = []
            if isKnown:
                state = ["1", "2", "3"]
                value.remove("1")
                value.remove("2")
                value.remove("3")
                for j in range(6):
                    random_value = random.choice(value)
                    state.append(random_value)
                    value.remove(random_value)
            else:
                for j in range(9):
                    random_value = random.choice(value)
                    state.append(random_value)
                    value.remove(random_value)
            list_state.append(state)
        return list_state
    
    # Hiển thị trạng thái ngẫu nhiên trong bảng
    def display_random_state(self):
        for i in range(8):
            for j in range(9):
                getattr(self, f"s{i}{j}").setText(self.list_start_state[i][j])
                getattr(self, f"d{i}{j}").setText(self.list_destination_state[i][j])

    def reset_state(self, algo):
        self.list_start_state = self.randomize_state()
        if algo == "Pos":
            self.list_destination_state = self.randomize_state(True)
        else:
            self.list_destination_state = self.randomize_state()
        self.current_step = 0
        for i in range(9):
            getattr(self, f"r0{i+1}").setText("")
        self.lblStep.setText("0")
        self.display_random_state()

    # NoObservation - Searching with No Observation
    def Nos(self):
        # Ngắt kết nối các nút trước đó nếu có
        if self.connection:
            self.btnStart.clicked.disconnect()
            self.btnReset.clicked.disconnect()
        self.lbl_title.setText("Searching with NoObservation")
        self.list_start_state = self.randomize_state()
        self.list_destination_state = self.randomize_state()
        self.btnStart.clicked.connect(self.NoObservation)
        self.btnReset.clicked.connect(lambda : self.reset_state("Nop"))
        self.connection = True
        self.display_random_state()

    def NoObservation(self):
        # Khởi tạo hàng đợi với các trạng thái bắt đầu
        queue = [Node(state) for state in self.list_start_state]
        # Tập hợp các trạng thái đã thăm
        visited = set()
        
        while queue:
            # Lấy trạng thái đầu tiên từ hàng đợi
            current_node = queue.pop(0)
            current_state = current_node.current_state
            
            # Kiểm tra xem đã đạt đến đích chưa
            if current_state in self.list_destination_state:
                self.result = current_node.Path()
                return self.Show()
            
            # Tạo tất cả các trạng thái kế tiếp
            for move in ["Up", "Down", "Left", "Right"]:
                new_state = self.move_state(current_state, move)
                t_state = tuple(map(tuple, new_state))
                # Chỉ thêm vào hàng đợi nếu trạng thái mới chưa được thăm
                if t_state not in visited:
                    visited.add(t_state)
                    # Tạo nút mới và thêm vào hàng đợi
                    queue.append(Node(new_state, current_node))
        
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng NoObservation!")

    # PartiallyObservation - Searching with Partially Observation
    def Pos(self):
        # Ngắt kết nối các nút trước đó nếu có
        if self.connection:
            self.btnStart.clicked.disconnect()
            self.btnReset.clicked.disconnect()
        self.lbl_title.setText("PartiallyObservation")
        self.list_start_state = self.randomize_state()
        self.list_destination_state = self.randomize_state(True)
        self.btnStart.clicked.connect(self.PartiallyObservation)
        self.btnReset.clicked.connect(lambda : self.reset_state("Pos"))
        self.connection = True
        self.display_random_state()

    def move_state(self, state: list, move: str) -> list:
        '''Trả về trạng thái mới sau khi di chuyển'''
        # Tạo bản sao của state để không ảnh hưởng state gốc
        new_state = state.copy()
        
        # Tìm vị trí ô trống
        empty_pos = -1
        for i in range(len(state)):
            if state[i] == "":
                empty_pos = i
                break
            
        # Xác định các vị trí có thể di chuyển
        moves = {
            "Up": empty_pos + 3 if empty_pos < 6 else -1,      # Ô dưới lên
            "Down": empty_pos - 3 if empty_pos > 2 else -1,    # Ô trên xuống
            "Left": empty_pos + 1 if empty_pos % 3 != 2 else -1,  # Ô phải sang trái
            "Right": empty_pos - 1 if empty_pos % 3 != 0 else -1  # Ô trái sang phải
        }
        
        # Thực hiện di chuyển nếu hợp lệ
        next_pos = moves[move]
        if next_pos != -1 and 0 <= next_pos < len(state):
            new_state[empty_pos] = new_state[next_pos]
            new_state[next_pos] = ""
            
        return new_state

    def is_valid(self, state: list) -> bool:
        '''Kiểm tra trạng thái có hợp lệ hay không'''
        for i in range(3):
            if state[i]!= i+1:
                return False
        return True

    def PartiallyObservation(self):
        list_valid_state = []
        list_valid_state = [Node(state) for state in self.list_start_state]
        moves = ["Up", "Down", "Left", "Right"]
        while list_valid_state:
            random_move = random.choice(moves)
            for state in list_valid_state:
                # Kiểm tra xem state hiện tại có phải là đích
                if state.current_state in self.list_destination_state:
                    self.result = state.Path()  # Lấy đường đi từ gốc đến đích
                    return self.Show()
                # Tạo trạng thái mới từ trạng thái hiện tại
                new_state = self.move_state(state.current_state, random_move)
                if self.is_valid(new_state):
                    list_valid_state.append(Node(new_state, state))
                list_valid_state.remove(state)
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Partially observation!")
        return None

    def Show(self):
        if self.result:
            self.current_step = 0 
            self.timer.start(500) 
    
    def update_ui(self):
        if self.current_step < len(self.result):  # Kiểm tra nếu chưa hết danh sách
            state = self.result[self.current_step]
            for i in range(9):
                getattr(self, f"r0{i+1}").setText(state[i])
                self.lblStep.setText(str(self.current_step))

            self.current_step += 1  # Chuyển sang bước tiếp theo
        else:
            self.timer.stop()  # Dừng timer khi đã hiển thị xong












