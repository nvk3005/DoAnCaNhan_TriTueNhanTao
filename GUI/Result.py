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
    execution_times = {}  

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def center(self):
        qr = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center()  
        qr.moveCenter(cp) 
        self.move(qr.topLeft()) 
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
        self.btn_Ga.clicked.connect(self.GeneticAlgorithm)
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
        start = time.perf_counter()
        queue = deque()
        visited = set()
        queue.append(Node(self.start_state))
        visited.add(tuple(map(tuple, self.start_state)))
        while queue:
            current = queue.popleft()
            if current.current_state == self.destination_state:
                end = time.perf_counter()
                self.execution_times["BFS"] = end - start
                self.result = current.Path()
                self.compare_algorithms["BFS"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    queue.append(Node(new_state, current))
        return None
    
    def Dfs_Solve(self):
        self.lbl_title.setText("DFS")
        start = time.perf_counter()
        stack = []
        visited = set()
        stack.append(Node(self.start_state))
        visited.add(tuple(map(tuple, self.start_state)))
        while stack:
            current = stack.pop()
            if current.current_state == self.destination_state:
                end = time.perf_counter()
                self.execution_times["DFS"] = end - start
                self.result = current.Path()
                self.compare_algorithms["DFS"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    stack.append(Node(new_state, current))
        return None
    
    def Ucs_Solve(self):
        self.lbl_title.setText("UCS")
        start = time.perf_counter()
        pre = PriorityQueue()
        visited = set()
        pre.put(Node(self.start_state))
        visited.add(tuple(map(tuple, self.start_state)))
        while not pre.empty():
            current = pre.get()
            if current.current_state == self.destination_state:
                end = time.perf_counter()
                self.execution_times["UCS"] = end - start
                self.result = current.Path()
                self.compare_algorithms["UCS"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    pre.put(Node(new_state, current, current.cost + 1))
        return None
    
    def Ids_Solve(self):
        self.lbl_title.setText("IDS")
        star = time.perf_counter()
        limit = 0
        while True:
            stack = [Node(self.start_state)]
            visited = set()
            visited.add(tuple(map(tuple, self.start_state)))
            while stack:
                current = stack.pop()
                if current.current_state == self.destination_state:
                    end = time.perf_counter()
                    self.execution_times["IDS"] = end - star
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
        start = time.perf_counter()
        pre = PriorityQueue()
        visited = set()
        pre.put(Node(self.start_state, h = self.heuristic(self.start_state)))
        visited.add(tuple(map(tuple, self.start_state)))
        while not pre.empty():
            current = pre.get()
            if current.current_state == self.destination_state:
                end = time.perf_counter()
                self.execution_times["Greedy"] = end - start
                self.result = current.Path()
                self.compare_algorithms["Greedy"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    pre.put(Node(new_state, current,  h = self.heuristic(new_state)))
        return None

    def AStar(self):
        self.lbl_title.setText("A*")
        start = time.perf_counter()
        pre = PriorityQueue()
        visited = set()
        pre.put(Node(self.start_state, h = self.heuristic(self.start_state), g = 0))
        visited.add(tuple(map(tuple, self.start_state)))
        while not pre.empty():
            current = pre.get()
            if current.current_state == self.destination_state:
                end = time.perf_counter()
                self.execution_times["A*"] = end - start
                self.result = current.Path()
                self.compare_algorithms["AStar"] = len(self.result)
                return self.Show()
            for new_state in self.generate_states(current.current_state):
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    pre.put(Node(new_state, current,  h = self.heuristic(new_state), g = current.g + 1))
        return None
    
    def ida_dfs_stack(self, threshold):
        stack = []
        start_node = Node(self.start_state, g=0, h=self.heuristic(self.start_state))
        stack.append(start_node)
        min_threshold = float('inf') # f-value nhỏ nhất vượt ngưỡng hiện tại
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
            visited.add(tuple(map(tuple, state))) 
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
        start = time.perf_counter()
        threshold = self.heuristic(self.start_state)
        while True:
            result = self.ida_dfs_stack(threshold)
            if isinstance(result, list):
                end = time.perf_counter()
                self.execution_times["IdaStar"] = end - start
                self.result = result
                self.compare_algorithms["IdaStar"] = len(result)
                return self.Show()
            if result == float('inf'):
                return None 
            threshold = result

    def SimpleHillClimbing(self):
        self.lbl_title.setText("Simple Hill Climbing")
        start = time.perf_counter()
        current_node = Node(self.start_state, h=self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            end = time.perf_counter()
            self.execution_times["SHC"] = end - start
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
                end = time.perf_counter()
                self.execution_times["SHC"] = end - start
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
        start = time.perf_counter()
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
                end = time.perf_counter()
                self.execution_times["SAHC"] = end - start
                self.result = next_node.Path()
                self.compare_algorithms["SAHC"] = len(self.result)
                return self.Show()
            current_node = next_node

    def StochasticHC(self):
        self.lbl_title.setText("Stochastic Hill Climbing")
        start = time.perf_counter()
        current_node = Node(self.start_state, h=self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            end = time.perf_counter()
            self.execution_times["StochasticHC"] = end - start
            self.result = current_node.Path()
            self.compare_algorithms["StochasticHC"] = len(self.result)
            return self.Show()
        max_iterations = 1000  # Số lần lặp tối đa
        for _ in range(max_iterations):
            neighbors = self.generate_states(current_node.current_state)
            neighbor_nodes = []
            for state in neighbors:
                h = self.heuristic(state)
                neighbor_nodes.append(Node(state, parent_node=current_node, h=h))
            better_neighbors = [node for node in neighbor_nodes if node.h < current_node.h]
            if not better_neighbors:
                # Nếu không có neighbor nào tốt hơn → KẾT THÚC TÌM KIẾM
                messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Stochastic Hill Climbing")
                return
            # Chọn ngẫu nhiên một neighbor tốt hơn
            next_node = random.choice(better_neighbors)
            if next_node.current_state == self.destination_state:
                end = time.perf_counter()
                self.execution_times["StochasticHC"] = end - start
                self.result = next_node.Path()
                self.compare_algorithms["StochasticHC"] = len(self.result)
                return self.Show()
            current_node = next_node
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Stochastic Hill Climbing)")

    def SimulatedAnnealing(self):
        self.lbl_title.setText("Simulated Annealing")
        start = time.perf_counter()
        current_node = Node(self.start_state, h=self.heuristic(self.start_state))
        temperature = 1000.0 # Nhiệt độ ban đầu
        cooling_rate = 0.99 # Tỷ lệ làm mát
        if current_node.current_state == self.destination_state:
            end = time.perf_counter()
            self.execution_times["SimulatedAnnealing"] = end - start
            self.result = current_node.Path()
            self.compare_algorithms["SimulatedAnnealing"] = len(self.result)
            return self.Show()
        while temperature > 1:
            neighbors = self.generate_states(current_node.current_state)
            if not neighbors:
                break 
            next_state = random.choice(neighbors)
            next_node = Node(next_state, current_node, h=self.heuristic(next_state))
            delta_cost = current_node.h - next_node.h
            # Nếu chi phí của giải pháp cũ lớn hơn giải pháp mới thì chọn giải pháp mới
            if delta_cost > 0 or random.uniform(0, 1) < math.exp(delta_cost / temperature):
                current_node = next_node
                if current_node.current_state == self.destination_state:
                    end = time.perf_counter()
                    self.execution_times["SimulatedAnnealing"] = end - start                
                    self.result = current_node.Path()
                    self.compare_algorithms["SimulatedAnnealing"] = len(self.result)
                    return self.Show()
            # Giảm nhiệt độ theo tỷ lệ cooling_rate
            temperature *= cooling_rate
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Simulated Annealing")
              
    def BeamSearch(self):
        self.lbl_title.setText("Beam Search")
        start = time.perf_counter()
        current_node = Node(self.start_state, h = self.heuristic(self.start_state))
        if current_node.current_state == self.destination_state:
            end = time.perf_counter()
            self.execution_times["BeamSearch"] = end - start
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
                    end = time.perf_counter()
                    self.execution_times["BeamSearch"] = end - start
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

    def GeneticAlgorithm(self):
        self.lbl_title.setText("Genetic Algorithm")
        # Các tham số
        population_size = 100
        generations = 50
        mutation_rate = 0.2
        elite_size = 10

        def calculate_fitness(individual):
            """Tính độ thích nghi của một cá thể"""
            h = 0
            for i in range(3):
                for j in range(3):
                    if individual[i][j] != '':
                        # Convert string to int before subtraction
                        value = int(individual[i][j])
                        goal_i = (value - 1) // 3
                        goal_j = (value - 1) % 3
                        h += abs(i - goal_i) + abs(j - goal_j)
            return 1 / (h + 1)  # Đảo ngược để có giá trị cao hơn cho giải pháp tốt

        def create_individual():
            """Tạo một cá thể ngẫu nhiên"""
            current = copy.deepcopy(self.start_state)
            moves = random.randint(10, 30)
            for _ in range(moves):
                next_states = self.generate_states(current)
                if next_states:
                    current = random.choice(next_states)
            return current

        def create_initial_population():
            """Khởi tạo quần thể ban đầu"""
            population = [copy.deepcopy(self.start_state)]
            while len(population) < population_size:
                individual = create_individual()
                population.append(individual)
            return population

        def selection(population, fitness_scores):
            """Chọn lọc cá thể cho thế hệ tiếp theo"""
            sorted_pop = [x for _, x in sorted(zip(fitness_scores, population), 
                                            key=lambda pair: pair[0], reverse=True)]
            elite = sorted_pop[:elite_size]
            selected = []
            fitness_sum = sum(fitness_scores)
            if fitness_sum == 0:
                return random.sample(population, population_size)
            probabilities = [f/fitness_sum for f in fitness_scores]
            while len(selected) + len(elite) < population_size:
                selected.append(random.choices(population, weights=probabilities, k=1)[0])
            return elite + selected

        def crossover(parent1, parent2):
            """Lai ghép hai cá thể cha mẹ"""
            child = copy.deepcopy(parent1)
            moves = random.randint(3, 8)
            current = copy.deepcopy(child)
            for _ in range(moves):
                next_states = self.generate_states(current)
                if next_states:
                    current = random.choice(next_states)
            return current

        def mutate(individual):
            """Đột biến một cá thể"""
            if random.random() < mutation_rate:
                mutated = copy.deepcopy(individual)
                moves = random.randint(1, 3)
                for _ in range(moves):
                    next_states = self.generate_states(mutated)
                    if next_states:
                        mutated = random.choice(next_states)
                return mutated
            return individual

        def create_next_generation(population, fitness_scores):
            """Tạo thế hệ tiếp theo"""
            selected = selection(population, fitness_scores)
            next_gen = []
            sorted_pop = [x for _, x in sorted(zip(fitness_scores, population), 
                                            key=lambda pair: pair[0], reverse=True)]
            next_gen.extend(sorted_pop[:elite_size])
            while len(next_gen) < population_size:
                parent1 = random.choice(selected)
                parent2 = random.choice(selected)
                child = crossover(parent1, parent2)
                child = mutate(child)
                next_gen.append(child)    
            return next_gen

        # Main algorithm
        start_time = time.perf_counter()
        current_population = create_initial_population()
        
        for generation in range(generations):
            fitness_scores = [calculate_fitness(individual) for individual in current_population]
            best_fitness = max(fitness_scores)
            best_index = fitness_scores.index(best_fitness)
            best_individual = current_population[best_index]
            
            if best_individual == self.destination_state:
                end_time = time.perf_counter()
                self.execution_times["GeneticAlgorithm"] = end_time - start_time
                self.result = [best_individual]
                self.compare_algorithms["GeneticAlgorithm"] = 1
                return self.Show()
                
            current_population = create_next_generation(current_population, fitness_scores)
        
        messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng Genetic Algorithm")
        return None
    
    def AOStar(self, max_depth=30):
        self.lbl_title.setText("AO*")
        start = time.perf_counter()
        visited = {}

        def OR_Search(state: list, path: list, depth: int):
            """
            Thực hiện tìm kiếm OR - tìm một trạng thái tiếp theo thành công
            """
            t_state = tuple(map(tuple, state))
            if state == self.destination_state:
                # Nếu tìm thấy trạng thái đích, trả về đường đi
                end = time.perf_counter()
                self.execution_times["AO*"] = end - start
                return path + [state]
            if state in path or depth > max_depth:
                return None
            if t_state in visited and visited[t_state] is not None:
                return visited[t_state]
            neighbors = self.generate_states(state)
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
            messagebox.showinfo("Thông báo", "Không tìm thấy lời giải bằng AO*")
            return None

    def Test(self):
        def is_consistent(value, assignment):
            # Kiểm tra xem value đã xuất hiện ở biến nào khác chưa
            for v in assignment.values():
                if v == value:
                    return False
            return True

        def backtracking(variables, domains, assignment={}):
            if len(assignment) == len(variables):
                return assignment  # Đã gán hết biến

            unassigned_vars = [v for v in variables if v not in assignment]
            var = unassigned_vars[0]

            for value in domains[var]:
                if is_consistent(value, assignment):
                    assignment[var] = value
                    result = backtracking(variables, domains, assignment)
                    if result:
                        return result
                    assignment.pop(var)
            return None

        # Biến là vị trí trên bảng 3x3
        variables = [f'X{i}' for i in range(9)]

        # Miền giá trị mỗi vị trí là các số 0-8 
        domains = {var: list(range(9)) for var in variables}

        # Bắt đầu thử gán
        solution = backtracking(variables, domains)

        print("Một trạng thái hợp lệ của bảng 8-puzzle:")
        for i in range(3):
            print([solution[f'X{3*i + j}'] for j in range(3)])

    
    isStart = False
    _start_time = 0
    def Backtracking(self, current_node, visited, max_depth=30):
        self.lbl_title.setText("Backtracking")
        
        if not self.isStart:
            self.isStart = True
            self._start_time = time.perf_counter()

        # Nếu đạt trạng thái đích
        if current_node.current_state == self.destination_state:
            end = time.perf_counter()
            self.execution_times["Backtracking"] = end - self._start_time
            self.result = current_node.Path()
            self.compare_algorithms["Backtracking"] = len(self.result)
            return True, self.Show()
        state_tuple = tuple(map(tuple, current_node.current_state))
        if state_tuple in visited or current_node.depth > max_depth:
            return False
        visited.add(state_tuple)
        for new_state in self.generate_states(current_node.current_state):
            next_tuple = tuple(map(tuple, new_state))
            if next_tuple not in visited:
                next_node = Node(new_state, current_node, depth=current_node.depth + 1)
                result = self.Backtracking(next_node, visited, max_depth)
                if result:
                    return True

        visited.remove(state_tuple)
        return False

    
    def AC3(self):
        from collections import deque
        import copy
        # Ràng buộc
        def different_constraint(x: int, y: int):
            return x != y
        
        # Hàm revise: Xét và điều chỉnh domain của Xi dựa vào ràng buộc với Xj
        def revise(domains: dict, Xi, Xj):
            revised = False
            for x in domains[Xi][:]:  
                if all(not different_constraint(x, y) for y in domains[Xj]):
                    domains[Xi].remove(x)
                    revised = True
            return revised

        # Thuật toán AC-3
        def ac3(domains: dict, neighbors: dict):
            # Tạo hàng đợi ban đầu chứa tất cả các cặp (Xi, Xj)
            queue = deque([(Xi, Xj) for Xi in domains for Xj in neighbors[Xi]])

            while queue:
                Xi, Xj = queue.popleft()
                if revise(domains, Xi, Xj):
                    # Nếu domain của Xi bị rỗng → không còn giá trị hợp lệ → không thể giải
                    if not domains[Xi]:
                        return False
                    # Nếu Xi bị thay đổi, ta cần kiểm tra lại các biến Xk có liên quan đến Xi
                    for Xk in neighbors[Xi]:
                        if Xk != Xj:
                            queue.append((Xk, Xi))
            return True

        # Khởi tạo danh sách biến (X0 đến X8)
        variables = [f'X{i}' for i in range(9)]

        # Miền giá trị ban đầu: tất cả các biến có thể nhận giá trị từ 1 đến 8
        domains = {var: list(range(1, 9)) for var in variables}

        # Gán cố định giá trị cho một số biến để kiểm tra AC-3
        domains['X0'] = [1]
        domains['X1'] = [3]
        domains['X2'] = [5]

        # Tạo danh sách các biến lân cận (mọi biến khác đều là hàng xóm)
        neighbors = {var: [v for v in variables if v != var] for var in variables}
        domains_copy = copy.deepcopy(domains)

        # In ra miền giá trị ban đầu
        print("Miền giá trị ban đầu:")
        for var in sorted(domains_copy):
            print(f"{var}: {domains_copy[var]}")
        
        # Chạy thuật toán AC-3
        has_result = ac3(domains_copy, neighbors)
        if has_result:
            print("Kết quả thuật toán AC-3:")
            for var in sorted(domains_copy):
                print(f"{var}: {domains_copy[var]}")
        else:
            print("Không tìm được lời giải hợp lệ (có domain rỗng).")


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
                reward = 10 if new_state == goal else -1 # Phần thưởng nếu đạt được trạng thái đích
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

        # Bắt đầu thuật toán Q-learning
        self.lbl_title.setText("Q-Learning")
        # Lấy trạng thái bắt đầu và đích
        start = convert_list_to_string(self.start_state)
        goal = convert_list_to_string(self.destination_state)

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
        start_time = time.perf_counter()
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
            
        end_time = time.perf_counter()
        self.execution_times["Q-learning"] = end_time - start_time
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
        self.compare_algorithms["Q-learning"] = len(path) - 1 
        
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
        
        # Tạo figure với 2 subplot
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Vẽ biểu đồ số bước
        steps = list(self.compare_algorithms.values())
        bars1 = ax1.bar(algorithms, steps, color='skyblue')
        
        # Ghi số bước lên đầu mỗi cột
        for bar, step in zip(bars1, steps):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, height + 0.5, 
                    str(step-1), ha='center', va='bottom', fontsize=10)
        
        ax1.set_xlabel("Thuật toán", fontsize=12)
        ax1.set_ylabel("Số bước", fontsize=12)
        ax1.set_title("So sánh số bước thực hiện", fontsize=14)
        ax1.tick_params(axis='x', rotation=30)

        # Vẽ biểu đồ thời gian
        times = [self.execution_times.get(algo, 0) for algo in algorithms]
        bars2 = ax2.bar(algorithms, times, color='lightgreen')
        
        # Ghi thời gian lên đầu mỗi cột
        for bar, t in zip(bars2, times):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2, height, 
                    f'{t:.3f}s', ha='center', va='bottom', fontsize=10)
        
        ax2.set_xlabel("Thuật toán", fontsize=12)
        ax2.set_ylabel("Thời gian (giây)", fontsize=12)
        ax2.set_title("So sánh thời gian thực thi", fontsize=14)
        ax2.tick_params(axis='x', rotation=30)

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
