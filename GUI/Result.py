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
        self.btn_AoStar.clicked.connect(lambda: self.AOStar(30))
        self.btn_Test.clicked.connect(self.Test)
        self.btn_Backtracking.clicked.connect(lambda: self.Backtracking(Node(self.start_state), visited=set()))
        self.btn_AC3.clicked.connect(self.AC3)
        self.btn_QLearning.clicked.connect(self.Q_Learning)

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
        self.lbl_title.setText("BFS")

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
        self.lbl_title.setText("DFS")

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
        self.lbl_title.setText("UCS")

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
        self.lbl_title.setText("IDS")

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
        self.lbl_title.setText("Greedy")

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
        self.lbl_title.setText("A*")

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
        self.lbl_title.setText("IDA*")
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
        self.lbl_title.setText("Simple Hill Climbing")
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
        self.lbl_title.setText("Steepest Ascent Hill Climbing")
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
        self.lbl_title.setText("Stochastic Hill Climbing")
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
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Stochastic Hill Climbing)")


    def SimulatedAnnealing(self):
        self.lbl_title.setText("Simulated Annealing")
        
        current_node = Node(self.start_state, h=self.heuristic(self.start_state))
        
        # Khởi tạo các biến cần thiết
        temperature = 1000.0
        cooling_rate = 0.99
        
        # Kiểm tra nếu trạng thái ban đầu đã là đích
        if current_node.current_state == self.destination_state:
            self.result = current_node.Path()
            self.compare_algorithms["SimulatedAnnealing"] = len(self.result)
            return self.Show()
        
        while temperature > 1:
            # Sinh ra một giải pháp lân cận ngẫu nhiên và tính chi phí của nó
            neighbors = self.generate_states(current_node.current_state)
            if not neighbors:
                break
            
            next_state = random.choice(neighbors)
            next_node = Node(next_state, current_node, h=self.heuristic(next_state))
            
            # So sánh chi phí giữa giải pháp mới và giải pháp cũ
            delta_cost = current_node.h - next_node.h
            
            # Nếu chi phí của giải pháp cũ lớn hơn giải pháp mới thì chọn giải pháp mới
            if delta_cost > 0 or random.uniform(0, 1) < math.exp(delta_cost / temperature):
                # Chấp nhận trạng thái mới
                current_node = next_node
        
                # Kiểm tra xem đã đạt đến đích chưa
                if current_node.current_state == self.destination_state:                
                    self.result = current_node.Path()
                    self.compare_algorithms["SimulatedAnnealing"] = len(self.result)
                    return self.Show()
            
            # Giảm nhiệt độ theo tỷ lệ cooling_rate
            temperature *= cooling_rate
        
        # Nếu không tìm thấy giải pháp, hiển thị thông báo
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Simulated Annealing")
              
    def BeamSearch(self):
        self.lbl_title.setText("Beam Search")
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

    def AOStar(self, max_depth=30):
        """
        Thuật toán AO* Search để tìm đường đi từ trạng thái bắt đầu đến trạng thái đích
        
        Parameters:
        - max_depth: Độ sâu tối đa được phép tìm kiếm
        
        Returns:
        - Kết quả của hàm Show() nếu tìm thấy đường đi, hoặc None nếu không tìm thấy
        """
        self.lbl_title.setText("AO*")
        
        # Dictionary lưu trữ các trạng thái đã thăm để tránh tính toán lại
        visited = {}
        
        def OR_Search(state: list, path: list, depth: int):
            """
            Thực hiện tìm kiếm OR - tìm một trạng thái tiếp theo thành công
            """
            # Chuyển state thành dạng hashable để sử dụng làm key trong dictionary
            t_state = tuple(map(tuple, state))
            
            # Debug để kiểm tra tiến trình (có thể bỏ comment khi cần debug)
            # print(f"OR_Search - Depth: {depth}, State: {state}")
            
            # Kiểm tra nếu đã đạt đến trạng thái đích
            if state == self.destination_state:
                return path + [state]
            
            # Phát hiện vòng lặp hoặc vượt quá độ sâu cho phép
            if state in path or depth > max_depth:
                return None
            
            # Kiểm tra nếu trạng thái này đã được thăm trước đó
            if t_state in visited and visited[t_state] is not None:
                return visited[t_state]
            
            # Lấy tất cả các trạng thái kề có thể đạt được
            neighbors = self.generate_states(state)
            
            # Đảm bảo neighbors không rỗng
            if not neighbors:
                visited[t_state] = None
                return None
            
            # Thử từng trạng thái kế tiếp cho đến khi tìm được đường đi thành công (OR)
            for neighbor in neighbors:
                result = AND_Search([neighbor], path + [state], depth + 1)
                if result is not None:
                    visited[t_state] = result  # Lưu result vào visited để sử dụng sau này
                    return result
            
            # Không tìm thấy đường đi thành công
            visited[t_state] = None
            return None
        
        def AND_Search(states, path, depth):
            """
            Thực hiện tìm kiếm AND - tất cả các trạng thái phải thành công
            """
            # Trường hợp cơ sở: không còn trạng thái nào cần kiểm tra
            if not states:
                return path
            
            full_path = path
            
            # Mỗi trạng thái trong danh sách phải thành công (AND)
            for state in states:
                result = OR_Search(state, full_path, depth)
                if result is None:
                    return None
                full_path = result
            
            return full_path
        
        # Bắt đầu tìm kiếm từ trạng thái khởi đầu
        result = OR_Search(self.start_state, [], 0)
        
        if result:
            self.result = result
            self.compare_algorithms["AO*"] = len(result)
            return self.Show()
        else:
            # Hiển thị thông báo khi không tìm thấy đường đi
            messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng AO*")
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

    def Q_Learning(self):
        import numpy as np
        import random
        import math

        # Các thông số Q-learning
        alpha = 0.3       # Tốc độ học
        gamma = 0.9       # Hệ số chiết khấu
        epsilon = 0.2     # Tỷ lệ khám phá
        episodes = 1000   # Số vòng học
        limitStep = 500   # Giới hạn số bước mỗi vòng

        # Tạo Q-table với 9! trạng thái, 4 hành động
        Q_table = np.zeros((math.factorial(9), 4))

        # 4 hướng di chuyển: lên, xuống, trái, phải
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Hàm chuyển đổi trạng thái từ list sang string
        def convert_list_to_string(state):
            return ''.join(state[i][j] if state[i][j] != '' else '0' 
                for i in range(3) 
                for j in range(3))

        def permutation_index(state):
            """
            Chuyển trạng thái thành chỉ số duy nhất bằng khai triển Cantor
            """
            state = list(state)
            index = 0
            for i in range(len(state)):
                # Chuyển đổi cả hai số thành int trước khi so sánh
                count = sum(1 for x in state[i+1:] if x != '0' and int(x) < int(state[i]))
                index += count * math.factorial(len(state) - i - 1)
            return index

        def take_action(state, action):
            """
            Thực hiện hành động và trả về trạng thái mới và phần thưởng
            """
            index = state.index('0')
            x, y = divmod(index, 3)
            dx, dy = action
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                state_list = list(state)
                state_list[index], state_list[new_index] = state_list[new_index], state_list[index]
                new_state = ''.join(state_list)
                reward = 10 if new_state == goal else -1
                return new_state, reward
            return state, -1  # Phạt nếu di chuyển không hợp lệ

        def choose_action(state):
            """Chọn hành động theo epsilon-greedy"""
            if random.uniform(0, 1) < epsilon:
                return random.choice(moves)
            else:
                state_idx = permutation_index(state)
                best_action = np.argmax(Q_table[state_idx])
                return moves[best_action]

        # Lấy trạng thái bắt đầu và đích
        start = convert_list_to_string(self.start_state)
        goal = convert_list_to_string(self.destination_state)

        print(f"Trạng thái bắt đầu: {start}")
        print(f"Trạng thái đích: {goal}")

        # Bắt đầu huấn luyện
        for episode in range(episodes):
            state = start
            for step in range(limitStep):
                idx = permutation_index(state)
                action = choose_action(state)
                next_state, reward = take_action(state, action)
                nidx = permutation_index(next_state)

                action_idx = moves.index(action)
                old_value = Q_table[idx, action_idx]
                next_max = np.max(Q_table[nidx])
                Q_table[idx, action_idx] += alpha * (reward + gamma * next_max - old_value)

                state = next_state
                if state == goal:
                    break

        # Tìm đường đi tốt nhất sau khi học xong
        state = start
        path = [start]
        visited = set([start])
        
        while state != goal:
            idx = permutation_index(state)
            action_idx = np.argmax(Q_table[idx])
            next_state, reward = take_action(state, moves[action_idx])
            
            if next_state in visited or next_state == state:
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Q-learning")
                return False, None
            
            path.append(next_state)
            visited.add(next_state)
            state = next_state
            
            if len(path) > 200:
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Q-learning")
                return False, None

        # Chuyển đổi đường đi từ chuỗi sang ma trận
        def convert_string_to_matrix(state_str):
            matrix = [['', '', ''] for _ in range(3)]
            for i in range(9):
                row, col = divmod(i, 3)
                if state_str[i] != '0':
                    matrix[row][col] = state_str[i]
            return matrix
        
        # Chuyển đổi đường đi từ chuỗi sang ma trận
        path_matrices = [convert_string_to_matrix(state_str) for state_str in path]
        
        self.result = path_matrices
        self.compare_algorithms["Q-learning"] = len(path) - 1  # Số bước di chuyển
        
        return True, self.Show()
        
    def Show(self):
        if self.result:
            self.current_step = 0 
            self.timer.start(500) 
    
    def update_ui(self):
        if self.current_step < len(self.result):
            state = self.result[self.current_step]
            
            # Kiểm tra nếu state là chuỗi (từ Q-Learning)
            if isinstance(state, str):
                # Chuyển chuỗi thành ma trận 3x3
                state_matrix = [
                    [state[i*3 + j] for j in range(3)]
                    for i in range(3)
                ]
                state = state_matrix
                
            # Cập nhật UI
            for i in range(3):
                for j in range(3):
                    self.labels[i][j].setText(state[i][j])
            self.lbl_Step.setText(str(self.current_step))
            
            self.current_step += 1
        else:
            self.timer.stop()

    import matplotlib.pyplot as plt

    def Graphic(self):
        algorithms = list(self.compare_algorithms.keys())
        steps = list(self.compare_algorithms.values())

        plt.figure(figsize=(10, 6))
        bars = plt.bar(algorithms, steps, color='skyblue')

        # Ghi số bước lên đầu mỗi cột
        for bar, step in zip(bars, steps):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, str(step-1), 
                    ha='center', va='bottom', fontsize=10, color='black')

        # Đặt tiêu đề và nhãn
        plt.xlabel("Thuật toán", fontsize=12)
        plt.ylabel("Số bước", fontsize=12)
        plt.title("Biểu đồ so sánh số bước thực hiện của các thuật toán tìm kiếm", fontsize=14)
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()


    def Reset_State(self):
        for i in range(3):
            for j in range(3):
                self.labels[i][j].setText(self.start_state[i][j])
        self.lbl_Step.setText('0')
        self.result = []
        self.lbl_title.setText("")
        QApplication.processEvents()
