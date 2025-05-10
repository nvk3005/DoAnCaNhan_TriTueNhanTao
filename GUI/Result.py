from collections import deque
import math
from queue import PriorityQueue
import copy
import random
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QFrame, QDesktopWidget
from GUI.ResultForm import Ui_Frame
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

    def center(self):
        qr = self.frameGeometry()  # Lấy hình chữ nhật bao quanh cửa sổ
        cp = QDesktopWidget().availableGeometry().center()  # Lấy tâm màn hình
        qr.moveCenter(cp)  # Di chuyển hình chữ nhật vào giữa
        self.move(qr.topLeft())  # Di chuyển cửa sổ đến điểm mới

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nguyễn Văn Kế - 23110234")
        self.center()

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
        self.btn_AoStar.clicked.connect(self.AOStar)
        self.btn_Test.clicked.connect(self.Test)
        self.btn_Backtracking.clicked.connect(lambda: self.Backtracking(Node(self.start_state), visited=set()))
        self.btn_AC3.clicked.connect(self.AC3)
        self.btn_QLearning.clicked.connect(self.QLearning)

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
    
    def ida_dfs_stack(self, threshold):
        stack = []
        start_node = Node(self.start_state, g=0, h=self.heuristic(self.start_state))
        stack.append(start_node)
        min_threshold = float('inf')

        visited = set() 

        while stack:
            current_node = stack.pop()
            state = current_node.current_state
            g = current_node.g
            f = g + self.heuristic(state)

            if f > threshold:
                min_threshold = min(min_threshold, f)
                continue

            if state == self.destination_state:
                return current_node.Path()

            visited.add(tuple(map(tuple, state)))  # Đánh dấu đã thăm

            for neighbor in self.generate_states(state):
                t_neighbor = tuple(map(tuple, neighbor))
                if t_neighbor in visited:
                    continue
                new_node = Node(
                    current_state=neighbor,
                    parent_node=current_node,
                    g=current_node.g + 1,
                    h=self.heuristic(neighbor)
                )
                stack.append(new_node)

        return min_threshold

    
    def IdaStar(self):
        threshold = self.heuristic(self.start_state)

        while True:
            result = self.ida_dfs_stack(threshold)
            if isinstance(result, list):  # Nếu trả về đường đi
                self.result = result
                self.compare_algorithms["IdaStar"] = len(result)
                return self.Show()
            if result == float('inf'):
                return None  # Không tìm được
            threshold = result  # Cập nhật ngưỡng mới


    def SimpleHillClimbing(self):
        current_node = Node(self.start_state, h=self.heuristic(self.start_state))

        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["SHC"] = len(self.result)
            return self.Show()

        while True:
            neighbors = self.generate_states(current_node.current_state)
            better_found = False

            for neighbor_state in neighbors:
                h_neighbor = self.heuristic(neighbor_state)
                if h_neighbor < current_node.h:  # Tốt hơn -> chọn
                    current_node = Node(
                        current_state=neighbor_state,
                        parent_node=current_node,
                        h=h_neighbor
                    )
                    better_found = True
                    break 

            if not better_found:
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
            if neighbor_score < best_score:  
                best_state = neighbor_state
                best_score = neighbor_score

        return best_state

    def SteepestAscentHillClimbing(self):
        current_node = Node(self.start_state, h=self.heuristic(self.start_state))

        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["SAHC"] = len(self.result)
            return self.Show()

        while True:
            next_state = self.get_best_neighbor(current_node.current_state)
            if next_state is None:
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Steepest Ascent Hill Climbing")
                return

            next_node = Node(next_state, parent_node=current_node, h=self.heuristic(next_state))

            if next_state == self.destination_state:
                self.result = next_node.Path()
                self.compare_algorithms["SAHC"] = len(self.result)
                return self.Show()

            current_node = next_node

    import random

    def StochasticHC(self):
        current_node = Node(self.start_state, h=self.heuristic(self.start_state))

        # Nếu trạng thái ban đầu là đích
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["StochasticHC"] = len(self.result)
            return self.Show()
        
        max_iterations = 1000  # Số lần lặp tối đa
        for _ in range(max_iterations):  # BƯỚC 5: Lặp lại trong n lần lặp
            # Tạo tất cả các trạng thái lân cận của trạng thái hiện tại
            neighbors = self.generate_states(current_node.current_state)

            # Đánh giá hàm mục tiêu tại tất cả các lân cận
            neighbor_nodes = []
            for state in neighbors:
                h = self.heuristic(state)
                neighbor_nodes.append(Node(state, parent_node=current_node, h=h))

            # So sánh với tất cả lân cận
            better_neighbors = [node for node in neighbor_nodes if node.h < current_node.h]

            if not better_neighbors:
                # Nếu không có neighbor nào tốt hơn → KẾT THÚC TÌM KIẾM
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Stochastic Hill Climbing")
                return

            # Chọn ngẫu nhiên một neighbor tốt hơn
            next_node = random.choice(better_neighbors)

            # Nếu tìm được lời giải
            if next_node.current_state == self.destination_state:
                self.result = next_node.Path()
                self.compare_algorithms["StochasticHC"] = len(self.result)
                return self.Show()

            # Chuyển sang trạng thái mới
            current_node = next_node

        # Trả về trạng thái hiện tại sau khi hết vòng lặp
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải sau số lần lặp cho phép (Stochastic Hill Climbing)")


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

    def AOStar(self):
        open_list = {}  
        closed_list = set() 
        
        initial_node = Node(self.start_state, h=self.heuristic(self.start_state))
        open_list[tuple(map(tuple, self.start_state))] = initial_node
        
        if initial_node.current_state == self.destination_state:
            self.result = initial_node.Path()
            self.compare_algorithms["AOStar"] = len(self.result)
            return self.Show()
        
        # Lặp cho đến khi tìm thấy đường đi hoặc không còn nút nào để mở
        while open_list:
            # Chọn nút có f = g + h nhỏ nhất
            current_key = min(open_list, key=lambda k: open_list[k].g + open_list[k].h)
            current_node = open_list.pop(current_key)
            
            closed_list.add(current_key)
            
            if current_node.current_state == self.destination_state:
                self.result = current_node.Path()
                self.compare_algorithms["AOStar"] = len(self.result)
                return self.Show()
            
            # Sinh ra các nút con
            children = []
            for new_state in self.generate_states(current_node.current_state):
                child_key = tuple(map(tuple, new_state))
                if child_key not in closed_list:
                    g_new = current_node.g + 1
                    h_new = self.heuristic(new_state)
                    
                    # Nếu nút con chưa có trong open_list hoặc có g mới tốt hơn
                    if child_key not in open_list or g_new < open_list[child_key].g:
                        # Tạo nút con mới và thêm vào open_list
                        child_node = Node(new_state, current_node, g=g_new, h=h_new)
                        open_list[child_key] = child_node
                        children.append(child_node)
            
            # Xử lý AND-OR logic, dùng OR node
            for child in children:
                if child.current_state == self.destination_state:
                    self.result = child.Path()
                    self.compare_algorithms["AOStar"] = len(self.result)
                    return self.Show()
        
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng AO* Search")
        return None

    def Test(self):
        pass
        
    def Backtracking(self, current_node, visited, max_depth = 30):
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["Backtracking"] = len(self.result)
            return True, self.Show()

        if current_node.depth > max_depth:
            return False

        visited.add(tuple(map(tuple, current_node.current_state)))

        for new_state in self.generate_states(current_node.current_state):
            t_state = tuple(map(tuple, new_state))
            if t_state not in visited:
                next_node = Node(new_state, current_node, depth=current_node.depth + 1)
                if self.Backtracking(next_node, visited):
                    return True

        visited.remove(tuple(map(tuple, current_node.current_state)))
        return False
    
    def AC3(self):
        pass

    def QLearning(self):
        import numpy as np
        
        # Hàm chuyển đổi trạng thái thành string để làm key cho Q-table
        def state_to_string(state):
            return ''.join(''.join(row) for row in state).replace('', '0')
        
        # Hàm chuyển đổi string trở lại thành trạng thái ma trận 3x3
        def string_to_state(state_str):
            state = [['', '', ''], ['', '', ''], ['', '', '']]
            for i in range(3):
                for j in range(3):
                    val = state_str[i*3 + j]
                    state[i][j] = val if val != '0' else ''
            return state
        
        # Các thông số cho Q-learning
        alpha = 0.1      # Tỷ lệ học tập
        gamma = 0.9      # Hệ số chiết khấu
        epsilon = 0.3    # Tỷ lệ thăm dò
        episodes = 1000  # Số lượng episodes
        
        # Khởi tạo Q-table ban đầu
        q_table = {}
        
        # Hàm trả về reward
        def get_reward(state):
            # Reward lớn nếu đạt đến trạng thái đích
            if state == self.destination_state:
                return 100
            
            # Reward dựa trên số ô đúng vị trí
            correct_tiles = 0
            for i in range(3):
                for j in range(3):
                    if state[i][j] == self.destination_state[i][j]:
                        correct_tiles += 1
            
            # Khuyến khích các trạng thái gần với trạng thái đích
            return correct_tiles - 5  # Adjust penalty to encourage progress
        
        # Hàm lấy các hành động hợp lệ từ trạng thái hiện tại
        def get_valid_actions(state):
            blank_i, blank_j = self.find_blank(state)
            valid_actions = []
            
            # Kiểm tra 4 hướng di chuyển (lên, xuống, trái, phải)
            for move in self.moves:
                new_i, new_j = blank_i + move[0], blank_j + move[1]
                if 0 <= new_i < 3 and 0 <= new_j < 3:
                    valid_actions.append(move)
            
            return valid_actions
        
        # Hàm thực hiện một hành động và trả về trạng thái mới
        def take_action(state, action):
            blank_i, blank_j = self.find_blank(state)
            new_i, new_j = blank_i + action[0], blank_j + action[1]
            
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in state]
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                return new_state
            
            return state  # Trả về trạng thái cũ nếu không thể di chuyển
        
        for episode in range(episodes):
            # Bắt đầu từ trạng thái ban đầu
            current_state = self.start_state
            
            # Đặt số bước tối đa cho mỗi episode
            max_steps = 100
            step = 0
            
            while step < max_steps:
                step += 1
                
                # Chuyển đổi trạng thái thành string để làm key cho Q-table
                state_str = state_to_string(current_state)
                
                # Lấy các hành động hợp lệ từ trạng thái hiện tại
                valid_actions = get_valid_actions(current_state)
                
                # Nếu trạng thái chưa có trong Q-table, khởi tạo các giá trị Q cho trạng thái đó
                if state_str not in q_table:
                    q_table[state_str] = {tuple(action): 0.0 for action in valid_actions}
                
                # Chọn hành động dựa trên chiến lược epsilon-greedy
                if np.random.uniform(0, 1) < epsilon:
                    # Thăm dò: chọn hành động ngẫu nhiên
                    action = valid_actions[np.random.choice(len(valid_actions))]
                else:
                    # Khai thác: chọn hành động có giá trị Q cao nhất
                    action_values = q_table[state_str]
                    # Lọc các hành động hợp lệ và chọn hành động tốt nhất
                    valid_action_values = {a: action_values.get(a, 0.0) for a in [tuple(va) for va in valid_actions]}
                    if valid_action_values:
                        action = max(valid_action_values, key=valid_action_values.get)
                    else:
                        action = valid_actions[np.random.choice(len(valid_actions))]
                
                # Thực hiện hành động và nhận trạng thái mới
                new_state = take_action(current_state, action)
                reward = get_reward(new_state)
                
                # Cập nhật Q-table
                new_state_str = state_to_string(new_state)
                
                # Nếu trạng thái mới chưa có trong Q-table, khởi tạo các giá trị Q cho trạng thái đó
                if new_state_str not in q_table:
                    new_valid_actions = get_valid_actions(new_state)
                    q_table[new_state_str] = {tuple(action): 0.0 for action in new_valid_actions}
                
                # Tính giá trị Q mới
                max_future_q = max(q_table[new_state_str].values()) if q_table[new_state_str] else 0
                current_q = q_table[state_str].get(tuple(action), 0.0)
                
                # Công thức cập nhật Q-value
                new_q = current_q + alpha * (reward + gamma * max_future_q - current_q)
                q_table[state_str][tuple(action)] = new_q
                
                # Cập nhật trạng thái hiện tại
                current_state = new_state
                
                # Nếu đạt đến trạng thái đích, kết thúc episode
                if current_state == self.destination_state:
                    print(f"Đã tìm thấy giải pháp sau {episode+1} episodes và {step} bước!")
                    break
            
            # Giảm epsilon theo thời gian để giảm dần việc thăm dò
            if episode % 100 == 0:
                epsilon = max(0.1, epsilon * 0.95)
        # Bắt đầu từ trạng thái ban đầu
        current_node = Node(self.start_state)
        
        # Số bước tối đa để tránh vòng lặp vô hạn
        max_steps = 100
        step = 0
        
        while step < max_steps and current_node.current_state != self.destination_state:
            step += 1
            state_str = state_to_string(current_node.current_state)
            
            if state_str in q_table:
                # Chọn hành động có giá trị Q cao nhất
                valid_actions = get_valid_actions(current_node.current_state)
                valid_action_tuples = [tuple(va) for va in valid_actions]
                
                # Lọc các hành động hợp lệ và chọn hành động tốt nhất
                valid_q_values = {a: q_table[state_str].get(a, 0.0) for a in valid_action_tuples}
                
                if valid_q_values:
                    best_action = max(valid_q_values, key=valid_q_values.get)
                    new_state = take_action(current_node.current_state, best_action)
                    new_node = Node(new_state, current_node)
                    current_node = new_node
                else:
                    print("Không tìm thấy hành động hợp lệ trong Q-table!")
                    break
            else:
                print(f"Trạng thái {state_str} không có trong Q-table!")
                break
        
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["Q-Learning"] = len(self.result)
            return self.Show()
        else:
            messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Q-Learning")
            return None
        
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
