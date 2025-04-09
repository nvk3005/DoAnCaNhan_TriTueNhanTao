from collections import deque
import math
from queue import PriorityQueue
import copy
import random
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QFrame
from ResultForm import Ui_Frame
import time
from Node import Node
import matplotlib.pyplot as plt
from tkinter import messagebox

class RESULT(QFrame, Ui_Frame):
    start_state = []
    destination_state = []
    result = []
    compare_algorithms = {}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nguyễn Văn Kế - 23110234")
        self.labels = [
            [self.cur_00, self.cur_01, self.cur_02],
            [self.cur_10, self.cur_11, self.cur_12],
            [self.cur_20, self.cur_21, self.cur_22]
        ]
        self.timer = QTimer()  
        self.timer.timeout.connect(self.update_ui) 
        self.btn_Bfs.clicked.connect(self.Bfs_Solve)
        self.btn_Dfs.clicked.connect(self.Dfs_Solve)
        self.btn_Ucs.clicked.connect(self.Ucs_Solve)
        self.btn_Ids.clicked.connect(self.Ids_Solve)
        self.btn_Greedy.clicked.connect(self.Greedy)
        self.btn_Astar.clicked.connect(self.AStar)
        self.btn_IdaStar.clicked.connect(self.IdaStar)
        self.btn_Sahc.clicked.connect(self.SteepestAscentHillClimbing)
        self.btn_Shc.clicked.connect(self.SimpleHillClimbing)
        self.btn_StochchaticHC.clicked.connect(self.StochasticHC)
        self.btn_Sa.clicked.connect(self.SimulatedAnnealing)
        self.btn_Bs.clicked.connect(self.BeamSearch)
        self.btn_Compare.clicked.connect(self.Graphic)
        self.btn_Reset.clicked.connect(self.Reset_State)


    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == '':
                    return i, j
    
    def generate_states(self, state):
        row, col = self.find_blank(state)
        new_states = []
        
        for move in self.moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = copy.deepcopy(state)
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                new_states.append(new_state)
        
        return new_states

    def Bfs_Solve(self):
        queue = deque()
        visited = set()

        queue.append(Node(self.start_state)) # Thêm vào cuối
        visited.add(tuple(map(tuple, self.start_state)))

        while queue:
            current = queue.popleft() # Lấy từ đầu 
            if current.current_state == self.destination_state:
                self.result = current.Path()
                self.compare_algorithms["BFS"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    queue.append(Node(new_state, current))
        return None # Trả về thông báo không tìm thấy kết quả
    
    def Dfs_Solve(self):
        stack = []
        visited = set()

        stack.append(Node(self.start_state))
        visited.add(tuple(map(tuple, self.start_state)))

        while stack:
            current = stack.pop()
            if current.current_state == self.destination_state:
                self.result = current.Path()
                self.compare_algorithms["DFS"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    stack.append(Node(new_state, current))
        return None # Trả về thông báo không tìm thấy kết quả
    
    def Ucs_Solve(self):
        pre = PriorityQueue()
        visited = set()

        pre.put(Node(self.start_state))
        visited.add(tuple(map(tuple, self.start_state)))

        while not pre.empty():
            current = pre.get()
            if current.current_state == self.destination_state:
                self.result = current.Path()
                self.compare_algorithms["UCS"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    pre.put(Node(new_state, current, current.cost + 1))

        return None # Trả về thông báo không tìm thấy kết quả
    
    
    def Ids_Solve(self):
        limit = 0
        while True:
            stack = [Node(self.start_state)]
            visited = set()
            visited.add(tuple(map(tuple, self.start_state)))
            while stack:
                current = stack.pop()
                if current.current_state == self.destination_state:
                    self.result = current.Path()
                    self.compare_algorithms["IDS"] = len(self.result)
                    return self.Show()
                if current.depth < limit:
                    for new_state in self.generate_states(current.current_state):
                        t_state = tuple(map(tuple, new_state))
                        if t_state not in visited:
                            visited.add(t_state)
                            stack.append(Node(new_state, current, depth=current.depth+1))
            limit += 1

    def heuristic(self, state):
        '''Hàm ước lượng chi phí đi từ trạng thái hiện tại đến trạng thái đích'''
        goal_position = {}

        for i in range(3):
            for j in range(3):
                goal_position[self.destination_state[i][j]] = (i, j)

        h = 0
        # Tính tổng khoảng cách Manhattan cho từng ô số
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    goal_x, goal_y = goal_position[value]
                    h += abs(i - goal_x) + abs(j - goal_y)

        return h


    def Greedy(self):
        pre = PriorityQueue()
        visited = set()

        pre.put(Node(self.start_state, h = self.heuristic(self.start_state)))
        visited.add(tuple(map(tuple, self.start_state)))

        while not pre.empty():
            current = pre.get()
            if current.current_state == self.destination_state:
                self.result = current.Path()
                self.compare_algorithms["Greedy"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    pre.put(Node(new_state, current,  h = self.heuristic(new_state)))

        return None # Trả về thông báo không tìm thấy kết quả

    def AStar(self):
        pre = PriorityQueue()
        visited = set()

        pre.put(Node(self.start_state, h = self.heuristic(self.start_state), g = 0))
        visited.add(tuple(map(tuple, self.start_state)))

        while not pre.empty():
            current = pre.get()
            if current.current_state == self.destination_state:
                self.result = current.Path()
                self.compare_algorithms["AStar"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    pre.put(Node(new_state, current,  h = self.heuristic(new_state), g = current.g + 1))

        return None # Trả về thông báo không tìm thấy kết quả

    def IdaStar(self):
        pre = PriorityQueue()
        i = 18
        while i:
            pre.put(Node(self.start_state, h = self.heuristic(self.start_state)))
            visited = set()
            visited.add(tuple(map(tuple, self.start_state)))
            while not pre.empty():
                current = pre.get()
                if current.current_state == self.destination_state:
                        self.result = current.Path()
                        self.compare_algorithms["IdaStar"] = len(self.result)
                        return self.Show()
                for new_state in self.generate_states(current.current_state):
                    t_state = tuple(map(tuple, new_state))
                    g_new = current.g + 1
                    f_new = g_new + self.heuristic(new_state)
                    if (f_new <= i and t_state not in visited):
                        pre.put(Node(new_state, current, g = g_new, h=self.heuristic(new_state)))
            i += 18

    def SimpleHillClimbing(self):
        current_node = Node(self.start_state, h = self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["SHC"] = len(self.result)
            return self.Show()

        while True:
            flag = False
            for neighbor_state in self.generate_states(current_node.current_state):
                if current_node.h < self.heuristic(neighbor_state):
                    current_node = Node(neighbor_state, current_node.current_state, h = self.heuristic(neighbor_state))
                    flag = True
                    break
            if (flag == False):
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Simple Hill Climbing")
                return 
            if current_node.current_state == self.destination_state:
                self.result = current_node.Path()
                self.compare_algorithms["SHC"] = len(self.result)
                return self.Show()


    def get_best_neighbor(self, state):
        '''Trả về trạng thái lân cận tốt nhất hoặc None nếu không có trạng thái nào tốt hơn'''
        best_state = None
        best_score = self.heuristic(state)

        for neighbor_state in self.generate_states(state):
            neighbor_score = self.heuristic(neighbor_state)
            if neighbor_score > best_score: 
                best_state = neighbor_state
                best_score = neighbor_score  

        return best_state 


    def SteepestAscentHillClimbing(self):
        current_node = Node(self.start_state, h = self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["SAHC"] = len(self.result)
            return self.Show()

        while True:
            next_state = self.get_best_neighbor(current_node.current_state)
            if next_state is None:
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Steepest Ascent HC")
                return
            if next_state == self.destination_state:
                self.result = current_node.Path()
                self.compare_algorithms["SHC"] = len(self.result)
                return self.Show()
            current_node = Node(next_state, current_node.current_state, h = self.heuristic(next_state))

    def StochasticHC(self):
        current_node = Node(self.start_state, h = self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["StockchasticHC"] = len(self.result)
            return self.Show()

        while True:
            neighbors = self.generate_states(current_node.current_state)
            better_neighbors = [n for n in neighbors if self.heuristic(n) > current_node.h]

            if not better_neighbors:
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Stochastic HC")
                return 
            current_state = random.choice(better_neighbors)
            current_node = Node(current_state, current_node.current_state, h = self.heuristic(current_state))
            if current_node.current_state == self.destination_state:
                self.result = current_node.Path()
                self.compare_algorithms["StockchasticHC"] = len(self.result)
                return self.Show()

    # Về viết Simulated Annealing, Beam Search  
    def SimulatedAnnealing(self):
        current_node = Node(self.start_state, h = self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["SimulatedAnnealing"] = len(self.result)
            return self.Show()

        temperature = 1000
        cooling_rate = 0.99

        while temperature > 1:
            neighbors = self.generate_states(current_node.current_state)
            next_state = random.choice(neighbors)

            delta_e = self.heuristic(next_state) - self.heuristic(current_node.current_state)
            if delta_e > 0 or random.uniform(0, 1) < math.exp(delta_e / temperature):
                current_node = Node(next_state, current_node.current_state, h = self.heuristic(next_state))

            if current_node.current_state == self.destination_state:
                self.result = current_node.Path()
                self.compare_algorithms["SimulatedAnnealing"] = len(self.result)
                return self.Show()

            temperature *= cooling_rate

        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Simulated Annealing")
              
    def BeamSearch(self):
        current_node = Node(self.start_state, h = self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["BeamSearch"] = len(self.result)
            return self.Show()
        beam_width = 2
        beam_list = [current_node]
        visited = set()
        visited.add(tuple(map(tuple, self.start_state)))

        while True:
            neighbors_beam = []
            if not beam_list:
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Beam Search")
                return
            for beam_node in beam_list:
                if beam_node.current_state == self.destination_state:
                    print(type(beam_node), beam_node)
                    self.result = beam_node.Path()
                    self.compare_algorithms["BeamSearch"] = len(self.result)
                    return self.Show()
                for neighbor in self.generate_states(beam_node.current_state):
                    t_state = tuple(map(tuple, neighbor))
                    if t_state not in visited:
                        visited.add(t_state)
                        neighbors_beam.append(Node(neighbor, beam_node, h = self.heuristic(neighbor)))    
            neighbors_beam.sort(key=lambda x: x.h)
            beam_list = neighbors_beam[:beam_width]
                

    def Show(self):
        if self.result:
            self.current_step = 0 
            self.timer.start(500) 
    
    def update_ui(self):
        if self.current_step < len(self.result):  # Kiểm tra nếu chưa hết danh sách
            state = self.result[self.current_step]
            for i in range(3):
                for j in range(3):
                    self.labels[i][j].setText(state[i][j])
                    self.lbl_Step.setText(str(self.current_step))

            self.current_step += 1  # Chuyển sang bước tiếp theo
        else:
            self.timer.stop()  # Dừng timer khi đã hiển thị xong
    def Graphic(self):
        algorithms = list(self.compare_algorithms.keys())
        steps = list(self.compare_algorithms.values())
        plt.bar(algorithms, steps, color='skyblue')
        plt.xlabel("Thuật toán")
        plt.ylabel("Số bước")
        plt.title("So sánh số bước của các thuật toán")
        plt.show()

    def Reset_State(self):
        for i in range(3):
            for j in range(3):
                self.labels[i][j].setText(self.start_state[i][j])
        self.lbl_Step.setText('0')
        self.result = []
        QApplication.processEvents()

