# 🤖 Đồ Án Cá Nhân - Trí Tuệ Nhân Tạo (Artificial Intelligence)


## 📑 Bảng nội dung

1. [Giới thiệu tổng quan về dự án](#-giới-thiệu-tổng-quan-về-dự-án)
2. [Các công nghệ dùng trong dự án](#%EF%B8%8F-các-công-nghệ-dùng-trong-dự-án)
3. [Cách thức hoạt động của dự án](#%EF%B8%8F-cách-thức-hoạt-động-của-dự-án)
4. [Cách chạy dự án](#%EF%B8%8F-cách-để-chạy-dự-án)
5. [Mục lục](#-mục-lục)


## 🧠 Giới thiệu tổng quan về dự án
Dự án được xây dựng nhằm mục đích nghiên cứu, đánh giá hiệu suất của các thuật toán thuộc các nhóm thuật toán khác nhau như Uninformed Search Algorithms, Informed Search Algorithms, Local Search Algorithms, Searching with Nondeterministic, Constraint Satisfaction Problem, Reinforcement Learning.
dựa trên việc áp dụng để giải quyết một vấn đề cụ thể là giải trò chơi "8-Puzzle".
> 👨‍💻 Dự án được thực hiện bởi [Nguyễn Văn Kế - MSSV: 23110234](https://github.com/nvk3005)

## 🛠️ Các công nghệ dùng trong dự án
- Python 3.10+
- Matplotlib
- Qt Designer (PyQt5)

## ⚙️ Cách thức hoạt động của dự án
Cấu trúc chương trình:
```
DoAnCaNhan_TriTueNhanTao/
├── GUI/
│   ├── Input.py: nhập trạng thái bắt đầu và trạng thái kết thúc
│   ├── InputForm.ui: file ui xây dựng bằng PyQT5
│   ├── Result.py: chứa mã nguồn các thuật toán của chương trình và chạy thuật toán ra giao diện
│   ├── ResultForm.py: file biên dịch từ file ui thành file .py để dùng như một thư viện
│   ├── ResultForm.ui: file ui xây dựng bằng PyQT5
│   ├── Search.py: chứa mã nguồn cho 2 thuật toán Searching with No Observation và Searching with Partially Observation
│   ├── SearchForm.py: file biên dịch từ file ui thành file .py để dùng như một thư viện
│   ├── SearchForm.ui: file ui xây dựng bằng PyQT5
│   ├── Steps.py: biểu diễn các bước tìm ra  lời giải của thuật toán
│   ├── StepsForm.py: file biên dịch từ file ui thành file .py để dùng như một thư viện
│   ├── StepsForm.ui: file ui xây dựng bằng PyQT5
├── Main.py: trang chính của chương trình nơi gọi các class và hỗ trợ chuyển đổi qua lại giữa các trang
├── Node.py: định nghĩa cấu trúc trạng thái và node trong thuật toán
├── .gitignore
├── README.md
```

Giao diện GUI của dự án được chia làm 4 trang chính:
- Trang Input: Cho phép người dùng nhập trạng thái bắt đầu và trạng thái đích
- Trang Result: Cho phép người dùng chọn thuật toán muốn áp dụng để tìm ra lời giải cho bài toán
- Trang Search: Áp dụng cho 2 thuật toán Searching with No Observation và Searching with Partially Observation
- Trang Steps: Hiển thị chi tiết từng bước tìm ra lời giải của thuật toán

## ▶️ Cách để chạy dự án.
1. Clone dự án từ GitHub:
   ```bash
   git clone https://github.com/nvk3005/DoAnCaNhan_TriTueNhanTao.git
   ```
2. Chạy file `Main.py` trong thư mục dự án:
   ```bash
   python Main.py
   ```
## 📊 Mục lục
### [A. Mục tiêu](#-mục-tiêu)
### [B. Nội dung](#-nội-dung)
- [I. Uninformed Search Algorithms](#i-uninformed-search-algorithms)
  - [1. Breadth-First Search](#1-breadth-first-search)
  - [2. Depth-First Search](#2-depth-first-search)
  - [3. Uniform Cost Search](#3-uniform-cost-search)
  - [4. Iterative Deepening Search](#4-iterative-deepening-search)
  - [5. Algorithm Performance Comparison](#5-algorithm-performance-comparison)
- [II. Informed Search Algorithms](#ii-informed-search-algorithms)
  - [1. A* Search](#1-a-search)
  - [2. Greedy Best-First Search](#2-greedy-best-first-search)
  - [3. Iterative Deepening A*](#3-iterative-deepening-a)
  - [4. Algorithm Performance Comparison](#4-algorithm-performance-comparison)
- [III. Local Search Algorithms](#iii-local-search-algorithms)
  - [1. Simple Hill Climbing](#1-simple-hill-climbing)
  - [2. Steepest Ascent Hill Climbing](#2-steepest-ascent-hill-climbing)
  - [3. Stochastic Hill Climbing](#3-stochastic-hill-climbing)
  - [4. Simulated Annealing](#4-simulated-annealing)
  - [5. Beam Search](#5-beam-search)
  - [6. GeneticAlgorithm](#6-geneticalgorithm)
  - [7. Algorithm Performance Comparison](#7-algorithm-performance-comparison)
- [IV. Searching with Nondeterministic](#iv-searching-with-nondeterministic)
  - [1. AND OR Search](#1-and-or-search)
  - [2. Searching with No Observation](#2-searching-with-no-observation)
  - [3. Searching with Partially Observation](#3-searching-with-partially-observation)
  - [4. Algorithm Performance Comparison](#4-algorithm-performance-comparison)
- [V. Constraint Satisfaction Problem](#v-constraint-satisfaction-problem)
  - [1. Test](#1-test)
  - [2. Backtracking](#2-backtracking)
  - [3. AC-3](#3-ac-3)
  - [4. Algorithm Performance Comparison](#4-algorithm-performance-comparison)
- [VI. Reinforcement Learning](vi-reinforcement-learning)
  - [1. Q-Learning](#1-q-learning)
  - [2. Algorithm Performance Comparison](#2-algorithm-performance-comparison)
### [C. Kết luận](#-kết-luận)

## A. Mục tiêu
  - Minh họa trực quan cách hoạt động của các thuật toán tìm kiếm và học tăng cường thông qua trò chơi 8-Puzzle.
  - Phân tích hiệu năng của từng thuật toán trong các nhóm:
    - Tìm kiếm không thông tin (Uninformed Search),
    - Tìm kiếm có thông tin (Informed Search),
    - Tìm kiếm cục bộ (Local Search),
    - Tìm kiếm trong môi trường không xác định (Nondeterministic Search),
    - Bài toán thỏa ràng ràng buộc (Constraint Satisfaction Problem),
    -Học tăng cường (Reinforcement Learning).
  - So sánh và đánh giá sự khác biệt về tốc độ, độ tối ưu và khả năng tìm ra lời giải giữa các thuật toán.
  - Cung cấp giao diện người dùng trực quan giúp tương tác với bài toán và quan sát quá trình giải quyết của từng thuật toán.
  - Nắm vững hơn các hiểu biết lý thuyết bằng cách thực hành và áp dụng vào bài toán cụ thể.

## B. Nội dung
## I. Uninformed Search Algorithms
| **Thành phần**       | **Mô tả**                                                                 |
|----------------------|---------------------------------------------------------------------------|
| Trạng thái bắt đầu   | Ma trận 3x3 với 8 số từ 1 đến 8 không trùng lặp và 1 ô trống              |
| Trạng thái mục tiêu  | Ma trận 3x3 với 8 số từ 1 đến 8 không trùng lặp và 1 ô trống, sắp xếp đúng thứ tự.              |
| Tập hành động        | Các hành động: UP, DOWN, LEFT, RIGHT (di chuyển ô trống tương ứng)       |
| Chi phí đường đi     | Mỗi hành động di chuyển có chi phí bằng 1                                |
| Lời giải           | Một chuỗi các hành động hợp lệ biến trạng thái ban đầu thành trạng thái mục tiêu |
### 1. Breadth-First Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/151c2746-571b-43fc-b87a-895e15e91b62)|<p>Steps: 23</p>|
### 2. Depth-First Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|None|<p>Steps: 7113</p>|
### 3. Uniform Cost Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/ee764cb5-a633-43e0-bfce-7eff3805b0fe)|<p>Steps: 23</p>|
### 4. Iterative Deepening Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/6809a94f-4b8b-46b9-8c24-b6c6a7f155d6)|<p>Steps: 27</p>|
### 5. Algorithm Performance Comparison
|Biểu đồ so sánh giữa các thuật toán trong nhóm Uninformed Search Algorithms|
| :--- |
|![Image](https://github.com/user-attachments/assets/b7a7f62c-9c8f-49dc-af04-2af7e8566244)|
#### BFS (Breadth-First Search):
- **BFS** cho lời giải với số bước rất ít (tối ưu), nhưng thời gian thực thi tương đối cao do phải duyệt rộng và lưu trữ nhiều trạng thái trong bộ nhớ.
#### DFS (Depth-First Search): 
- **DFS** có tốc độ thực thi rất nhanh nhờ đi sâu liên tục, nhưng số bước thực hiện lại rất lớn, cho thấy thuật toán dễ đi vào nhánh không tối ưu và không đảm bảo lời giải ngắn nhất.
#### IDS (Iterative Deepening Search):
- **IDS** có số bước gần với tối ưu và thời gian thực thi khá tốt, nhờ kết hợp lợi thế của **DFS** và **BFS**.
#### USC (Uniform Cost Search)
- **UCS** cũng cho lời giải tối ưu về số bước như BFS, nhưng thời gian thực thi cao nhất trong các thuật toán do phải quản lý hàng đợi ưu tiên và kiểm tra chi phí liên tục.

## II. Informed Search Algorithms
| **Thành phần**        | **Mô tả**                                                                 |
|------------------------|---------------------------------------------------------------------------|
| Trạng thái bắt đầu     | Ma trận 3x3 với 8 số từ 1 đến 8 và 1 ô trống                              |
| Trạng thái mục tiêu    | Ma trận 3x3 với 8 số từ 1 đến 8 không trùng lặp và 1 ô trống, sắp xếp theo đúng thứ tự.              |
| Tập hành động          | Các hành động: UP, DOWN, LEFT, RIGHT (di chuyển ô trống tương ứng)       |
| Chi phí đường đi       | Mỗi hành động di chuyển có chi phí bằng 1                                |
| Hàm heuristic h(n)     | Dự đoán chi phí còn lại từ trạng thái hiện tại `n` đến trạng thái đích   |
| Lời giải           | Chuỗi các hành động hợp lệ biến trạng thái ban đầu thành trạng thái mục tiêu |

### 1. A* Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/52df5071-a7da-4f82-a511-41ac1315c885)|<p>Steps: 23</p>|
### 2. Greedy Best-First Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/6da5f398-03d1-41cf-a93b-33e851de5032)|<p>Steps: 47</p>|
### 3. Iterative Deepening A*
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/1c6a6b4e-a560-46e6-9a5d-f7e39f9a2e73)|<p>Steps: 23</p>|
### 4. Algorithm Performance Comparison
|Biểu đồ so sánh giữa các thuật toán trong nhóm Informed Search Algorithms|
| :--- |
|![Image](https://github.com/user-attachments/assets/5c686a0c-cdd0-41d6-acb4-b5432981beac)|
#### A* Search
- **A\*** là thuật toán hiệu quả nhất: cho đường đi tối ưu (**23 bước**) và thời gian thực thi gần như tức thời (0.000s), nhờ kết hợp giữa chi phí thực tế (g) và chi phí ước lượng heuristic (h).
#### Greedy Best-First Search
- **Greedy** có thời gian thực thi nhanh (0.012s) nhưng phải qua nhiều bước hơn (**47 bước**) vì chỉ xét hàm heuristic mà không quan tâm đến chi phí thực tế, nên không đảm bảo tối ưu.
#### Iterative Deepening A*
- **IDA\*** cũng tìm đường đi tối ưu (23 bước) như **A\***, nhưng thời gian thực thi lâu hơn (0.099s) do phải lặp lại nhiều vòng lặp sâu dần

## III. Local Search Algorithms
| **Thành phần**        | **Mô tả**                                                                 |
|-------------------|------------------------------------------------------------------------|
| Trạng thái bắt đầu | Ma trận 3x3 gồm 8 số từ 1 đến 8 (không trùng) và 1 ô trống.                         |
| Trạng thái mục tiêu| Ma trận 3x3 gồm 8 số từ 1 đến 8 (không trùng) và 1 ô trống, sắp xếp đúng thứ tự. |
| Tập hành động      | Gồm các hành động: UP, DOWN, LEFT, RIGHT (di chuyển ô trống tương ứng). |
| Trạng thái lân cận | Các trạng thái có thể đạt được từ trạng thái hiện tại bằng 1 bước di chuyển. |
| Hàm đánh giá       | Hàm đo "độ tốt" của trạng thái, ví dụ như số ô sai vị trí hoặc khoảng cách Manhattan. |
| Lời giải| Một chuỗi các hành động hợp lệ biến trạng thái ban đầu thành trạng thái mục tiêu. |

### 1. Simple Hill Climbing
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/6a47e5ed-52c7-4264-b198-463ce933b627)|<p>Không tìm ra lời giải đến trạng thái đích</p>|
### 2. Steepest Ascent Hill Climbing
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/c4e8a933-4779-4ab3-a035-a44c5cc2a035)|<p>Không tìm ra lời giải đến trạng thái đích</p>|
### 3. Stochastic Hill Climbing
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/fa2f028f-7a6a-4beb-a4a7-7c1913d4a94f)|<p>Không tìm ra lời giải đến trạng thái đích</p>|
### 4. Simulated Annealing
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/505f250c-5249-47aa-af78-072def09f637)|<p>Không tìm ra lời giải đến trạng thái đích</p>|
### 5. Beam Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/f629404c-51cf-4575-8a29-900e57af9f50)|<p>Steps: 133</p>|
### 6. GeneticAlgorithm
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/15550e90-7288-444e-9e74-8cde99ca11b1)|<p>Không tìm ra lời giải đến trạng thái đích</p>|
### 7. Algorithm Performance Comparison
|Biểu đồ so sánh giữa các thuật toán trong nhóm Local Search Algorithms|
| :--- |
|![Image](https://github.com/user-attachments/assets/6f4698f5-16d6-491f-a56d-7b7550fef442)|
#### Simple Hill Climbing, Steepest Ascent Hill Climbing, Stochastic Hill Climbing, Simulated Annealing, GeneticAlgorithm
- Các thuật toán thuộc nhóm Local Search như trên thường không hiệu quả khi áp dụng cho bài toán 8-Puzzle, do đặc thù không gian trạng thái của bài toán có nhiều điểm cực trị địa phương:
  - Hill Climbing chỉ tiếp tục nếu tìm được trạng thái tốt hơn trạng thái hiện tại, nên dễ bị kẹt ở các điểm không phải tối ưu toàn cục và không có cơ chế quay lui.
  - Steepest Ascent Hill Climbing chọn trạng thái tốt nhất trong các hàng xóm, nhưng vẫn dễ rơi vào local optimum.
  - Stochastic Hill Climbing giảm xác suất mắc kẹt bằng cách chọn ngẫu nhiên một hàng xóm tốt, nhưng vẫn không đảm bảo tìm được lời giải.
  - Simulated Annealing có thể thoát khỏi local optima nhờ xác suất chấp nhận nghiệm xấu, nhưng hiệu quả phụ thuộc vào lịch làm nguội (cooling schedule).
  - Genetic Algorithm thường không hiệu quả với bài toán 8-Puzzle do khó thiết kế hàm đánh giá phù hợp và dễ sinh ra cá thể không hợp lệ trong không gian tìm kiếm lớn.
#### Beam Search
- Beam Search tìm ra lời giải sau 133 bước, số bước lớn cho thấy lời giải không tối ưu. Dù thời gian thực thi khá nhanh (0.017s), thuật toán dễ bỏ sót trạng thái tiềm năng do chỉ giữ lại số lượng giới hạn trạng thái tốt nhất ở mỗi bước. Vì vậy, hiệu quả phụ thuộc nhiều vào giá trị hàm heuristic và độ may mắn.

## IV. Searching with Nondeterministic
| **Thành phần**             | **Mô tả**                                                                                   |
|----------------------------|---------------------------------------------------------------------------------------------|
| Trạng thái bắt đầu         | Trạng thái khởi đầu có thể quan sát được một phần hoặc đầy đủ                               |
| Trạng thái mục tiêu        | Trạng thái mong muốn đạt đến            |
| Tập hành động              | Các hành động có thể thực hiện từ một trạng thái – có thể dẫn đến nhiều kết quả khác nhau   |
| Mô hình trạng thái | Mỗi hành động không chắc chắn dẫn đến 1 trạng thái, mà có thể dẫn đến **tập các trạng thái kế tiếp** |
| Kiến thức về môi trường    | Có thể **không đầy đủ** (partial knowledge) → phải tính đến mọi tình huống có thể xảy ra    |
| Chiến lược tìm kiếm        | Không phải chuỗi hành động, mà là **cây kế hoạch** (plan tree), gồm các hành động và nhánh kết quả |
| Lời giải                  | Một **kế hoạch điều kiện** (contingency plan): cho biết nên làm gì trong từng tình huống xảy ra |

### 1. AND OR Search
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/33167a86-f488-434b-8163-98af4d940279)|<p>Steps: 31</p>|
### 2. Searching with No Observation
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/a1eeb32a-eaf9-4f36-9583-3f7868329e37)|![Image](https://github.com/user-attachments/assets/a8281eaa-d9fa-4758-9f21-41ed7f5935c0)|<p>Steps: 10</p>|
### 3. Searching with Partially Observation
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/3c4e28f4-10e0-48e8-bd2d-b01870909915)|![Image](https://github.com/user-attachments/assets/e88b0db4-1ebc-45fe-a3d8-70c1d58487ad)|<p>Không tìm ra lời giải đến trạng thái đích</p>|
### 4. Algorithm Performance Comparison
|Biểu đồ so sánh giữa các thuật toán trong nhóm Searching with Nondeterministic|
| :--- |
|![Image](https://github.com/user-attachments/assets/155eede9-6d2d-400a-b880-9398b55a157b)|
#### AND OR Search
- **AO\*** đã tìm ra lời giải sau 31 bước cho thấy thuật toán đã hoạt động hiệu quả bằng cách sử dụng kết hợp AND và OR trong tìm kiếm, phù hợp với bài toán có cấu trúc rẽ nhánh và cần đánh giá nhiều khả năng kế tiếp. Bên cạnh đó nhờ việc sử dụng visited giúp tránh trạng thái đã thăm, giảm thiểu lặp vô hạn và tăng hiệu quả tìm kiếm. Đồng thời giới hạn độ sâu để tránh lan rộng không kiểm soát
#### Searching with No Observation
- Trong bài toán này, cả trạng thái đầu và trạng thái đích đều được khởi tạo ngẫu nhiên, và thuật toán không được cung cấp bất kỳ thông tin nào về trạng thái mục tiêu trong quá trình tìm kiếm. Do không loại bỏ bất kỳ trạng thái nào trong không gian tìm kiếm, thuật toán có thể duyệt qua toàn bộ không gian trạng thái. Điều này góp phần làm tăng xác suất tìm ra lời giải, mặc dù chi phí tính toán có thể lớn.
#### Searching with Partially Observation
- Thuật toán này cũng random ra 8 trạng thái đầu nhưng khác biệt so với **Searching with No Observation** là có nhìn thấy 1 phần của trạng thái đích nên sau mỗi bước chạy các trạng thái không thỏa mãn phần thông tin nhìn thấy được sẽ bị loại bỏ dẫn đến khả năng tìm ra lời giải tương đối thấp

## V. Constraint Satisfaction Problem
| **Thành phần**        | **Mô tả**                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------|
| Biến (Variables)      | Tập hợp các biến cần gán giá trị                                          |
| Miền giá trị (Domains) | Tập hợp các giá trị có thể gán cho mỗi biến          |
| Ràng buộc (Constraints) | Các điều kiện liên quan giữa các biến, giới hạn các giá trị có thể gán đồng thời           |
| Trạng thái             | Một phép gán giá trị cho một số biến (có thể là một phần hoặc toàn bộ biến)                |
| Lời giải   | Một phép gán giá trị cho tất cả các biến sao cho thoả mãn tất cả các ràng buộc              |

### 1. Test
| **Mục đích**                                         | **Kết quả thực thi**                                                                                       |
|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| Tạo ra một cấu hình hợp lệ cho bảng 8-puzzle bằng cách gán các số từ 0-8 vào 9 ô sao cho mỗi số chỉ xuất hiện một lần | Một trạng thái hợp lệ của bảng 8-puzzle:<br>[0, 1, 2]<br>[3, 4, 5]<br>[6, 7, 8]                            |
### 2. Backtracking
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/a02cf679-d815-4b9f-85f5-f40afd25fef0)|<p>Steps: 31</p>|
### 3. AC-3
| **Mục đích** | **Kết quả thực thi** |
|:-------------|:----------------------|
| Đảm bảo tính nhất quán cung (arc consistency) giữa các biến trong bài toán 8-puzzle, kiểm tra và loại bỏ các giá trị không thỏa mãn ràng buộc từ miền giá trị (domain) của các biến | Miền giá trị ban đầu:<br>X0: [1]<br>X1: [3]<br>X2: [5]<br>X3: [1, 2, 3, 4, 5, 6, 7, 8]<br>X4: [1, 2, 3, 4, 5, 6, 7, 8]<br>X5: [1, 2, 3, 4, 5, 6, 7, 8]<br>X6: [1, 2, 3, 4, 5, 6, 7, 8]<br>X7: [1, 2, 3, 4, 5, 6, 7, 8]<br>X8: [1, 2, 3, 4, 5, 6, 7, 8]<br><br>Kết quả thuật toán AC-3:<br>X0: [1]<br>X1: [3]<br>X2: [5]<br>X3: [2, 4, 6, 7, 8]<br>X4: [2, 4, 6, 7, 8]<br>X5: [2, 4, 6, 7, 8]<br>X6: [2, 4, 6, 7, 8]<br>X7: [2, 4, 6, 7, 8]<br>X8: [2, 4, 6, 7, 8] |
### 4. Algorithm Performance Comparison
|Biểu đồ so sánh giữa các thuật toán trong nhóm Constraint Satisfaction Problem|
| :--- |
|![Image](https://github.com/user-attachments/assets/06e8fd3f-2b8f-4ebb-a28c-98ce8f550974)|
- Thuật toán Backtracking tìm ra lời giải với số bước không quá lớn (31 bước), nhưng thời gian thực thi là không tối ưu cho những trường hợp phức tạp do tính chất kiểm tra đệ quy và loại bỏ trạng thái.

## VI. Reinforcement Learning
| **Thành phần**             | **Mô tả**                                                                                   |
|----------------------------|---------------------------------------------------------------------------------------------|
| Trạng thái bắt đầu         | Ma trận 3x3 với 8 số từ 1 đến 8 và 1 ô trống                                                |
| Trạng thái mục tiêu        | Ma trận 3x3 với 8 số từ 1 đến 8 không trùng lặp và 1 ô trống, sắp xếp đúng thứ tự.                                |
| Tập hành động              | Gồm các hành động: UP, DOWN, LEFT, RIGHT (di chuyển ô trống tương ứng)                     |
| Hàm phần thưởng            | Hàm xác định phần thưởng nếu đến trạng thái đích và bị phạt nếu đi sai    |
| Hệ số chiết khấu (γ)       | Hệ số chiết khấu giá trị phần thưởng tương lai, giúp cân bằng giữa hiện tại và tương lai   |
| Tốc độ học (α)             | Xác định mức độ cập nhật giá trị Q(s, a) sau mỗi hành động                                  |
| Q_table                    | Bảng lưu giá trị Q(s, a) cho mỗi cặp trạng thái và hành động                                |
| Chính sách hành động       | Sử dụng epsilon-greedy để cân bằng giữa khai thác (exploit) và khám phá (explore)          |
| Lời giải                   | Một chuỗi các hành động hợp lệ biến trạng thái ban đầu thành trạng thái mục tiêu           |

### 1. Q-Learning
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/932fff57-15c1-4738-add6-3020f35b23b8)|<p>Không tìm ra lời giải đến trạng thái đích</p>|

### 2. Algorithm Performance Comparison
#### Q-Learning
- Thuật toán Q-Learning không thể tìm ra lời giải cho game 8 Puzzle với trạng thái đã khởi tạo điều này có thể do 1 số lý do như chưa đủ số vòng lặp học (episodes). Số lượng trạng thái của game lớn nên có thể agent chưa từng đi con đường đó trong quá trình training → Q-table có thể không đủ thông tin để tìm được đường đi.

## Kết luận
  - Thông qua quá trình thực hiện dự án áp dụng các thuật toán giải bài toán 8 Puzzle, tôi đã có cơ hội ôn tập và hệ thống lại những kiến thức đã được học trên lớp một cách hiệu quả. Việc trực tiếp triển khai và theo dõi quá trình hoạt động của từng thuật toán không chỉ giúp tôi nắm vững cách cài đặt mà còn hiểu sâu hơn về cơ chế hoạt động của chúng. Đặc biệt, dự án đã giúp tôi nhận ra rõ ràng những ưu điểm và hạn chế của từng thuật toán, từ đó rút ra được bài học kinh nghiệm trong việc lựa chọn và áp dụng thuật toán phù hợp cho từng bài toán cụ thể.

