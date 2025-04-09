class Node:
    def __init__(self, current_state, parent_node=None, cost = 0, depth = 0, g = 0, h = 0):
        self.current_state = current_state
        self.parent_node = parent_node
        self.cost = cost
        self.depth = depth
        self.g = g
        self.h = h
    
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.g + self.h < other.g + other.h
        return self.cost < other.cost 

    def Path(self):
        path = []
        current_node = self
        while current_node is not None:
            path.append(current_node.current_state)
            current_node = current_node.parent_node  # Đi ngược lại nút cha
        return path[::-1]  # Đảo ngược để có thứ tự từ đầu đến cuối
