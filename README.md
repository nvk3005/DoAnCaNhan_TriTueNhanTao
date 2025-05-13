# 🤖 Đồ Án Cá Nhân - Trí Tuệ Nhân Tạo (Artificial Intelligence)


## 📑 Bảng nội dung

1. [Giới thiệu tổng quan về dự án](#-giới-thiệu-tổng-quan-về-dự-án)
2. [Các công nghệ dùng trong dự án](#%EF%B8%8F-các-công-nghệ-dùng-trong-dự-án)
3. [Cách thức hoạt động của dự án](#%EF%B8%8F-cách-thức-hoạt-động-của-dự-án)
4. [Cách chạy dự án](#%EF%B8%8F-cách-để-chạy-dự-án)
5. [Các thuật toán được sử dụng trong dự án](#-các-thuật-toán-được-sử-dụng-trong-dự-án)

## 🧠 Giới thiệu tổng quan về dự án
Dự án được xây dựng nhằm mục đích nghiên cứu, đánh giá hiệu suất của các thuật toán thuộc các nhóm thuật toán khác nhau như Uninformed Search Algorithms, Informed Search Algorithms, Local Search Algorithms, Searching with Nondeterministic, Constraint Satisfaction Problem, Reinforcement Learning.
dựa trên việc áp dụng để giải quyết một vấn đề cụ thể là giải trò chơi "8-Puzzle".
> 👨‍💻 Dự án được thực hiện bởi [Nguyễn Văn Kế - MSSV: 23110234](https://github.com/nvk3005)

## 🛠️ Các công nghệ dùng trong dự án
- Python 3.10+
- Matplotlib
- Qt Designer (PyQt5)

## ⚙️ Cách thức hoạt động của dự án
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
## 📊 Các thuật toán được sử dụng trong dự án

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
  - [6. Algorithm Performance Comparison](#6-algorithm-performance-comparison)
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

## I. Uninformed Search Algorithms
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
|Biểu đồ so sánh số bước giữa các thuật toán trong nhóm Uninformed Search Algorithms|
| :--- |
|![Image](https://github.com/user-attachments/assets/6cb02bff-5702-4076-a325-583bfc1a42fd)|
#### BFS (Breadth-First Search) và UCS (Uniform Cost Search):
- Đều đạt số bước giải khá nhỏ **23** bước cho thấy việc áp dụng 2 thuật toán này để tìm ra lời giải là khá tối ưu. Trong bài toán này chi phí mỗi bước đều bằng nhau và bằng 1 nên **UCS** cũng được áp dụng như **BFS**
#### DFS (Depth-First Search): 
- Cần tới **7113** bước để tìm ra lời giải cho thấy việc không hiệu khi đi sâu vào nhánh không tối ưu.
#### IDS (Iterative Deepening Search):
- Cần **27** bước để tìm ra lời giải cho thấy sự hiệu quả của việc cải tiến thuật toán DFS bằng cách giới hạn độ sâu tìm kiếm.

## II. Informed Search Algorithms
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
|Biểu đồ so sánh số bước giữa các thuật toán trong nhóm Informed Search Algorithms|
| :--- |
|![Image](https://github.com/user-attachments/assets/f0540d87-0c90-41d3-b81a-9c032c788fa5)|
#### A* Search
- Việc kết hợp chi phí thực tế g và chi phí ước tính h thuật toán A* đã tìm ra đường đi tối ưu cả về số bước (**23** bước) và thời gian tìm ra lời giải của thuật toán.
#### Greedy Best-First Search
- Thuật toán này mất **47** bước để tìm ra lời giải, số bước nhiều hơn A* vì thuật toán chỉ xét hàm heuristic h(n), bỏ qua chi phí thực tế. Nên bài toán thuật toán chỉ tìm ra lời giải nhanh chứ không xét tới tính tối ưu.
#### Iterative Deepening A*
- Cũng tìm đường đi tối ưu như A* sau (**23** bước), nhưng sử dụng ít bộ nhớ hơn do dựa trên tìm kiếm theo chiều sâu.

## III. Local Search Algorithms
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
### 6. Algorithm Performance Comparison
|Biểu đồ so sánh số bước giữa các thuật toán trong nhóm Local Search Algorithms|
| :--- |
|![Image](https://github.com/user-attachments/assets/ccfcb007-10ec-477e-996f-f512f2982869)|
#### Simple Hill Climbing, Steepest Ascent Hill Climbing, Stochastic Hill Climbing, Simulated Annealing
- Các thuất toán nhóm Local Search này áp dụng cho game 8 Puzzle đều không thể tìm ra lời giải vì dễ bị mắc kẹt ở **Local optimum (cực trị địa phương)**. Các thuật này chỉ hoạt động nếu tìm được trạng thái tốt hơn trạng thái hiện tại nếu không thuật toán sẽ dừng lại. 
#### Beam Search
- Beam Search tìm ra lời giải sau 133 bước. Beam Search sẽ giữ lại k trạng thái tốt nhất ở mỗi bước, dựa trên giá trị hàm heuristic đánh giá mức độ gần với trạng thái đích, và loại bỏ các trạng thái còn lại, kể cả khi chúng có tiềm năng dẫn đến lời giải. Nên nếu may mắn vẫn có thể tìm ra lời giải nhưng sẽ không tối ưu

## IV. Searching with Nondeterministic
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
#### AND OR Search
- **AO\*** đã tìm ra lời giải sau 31 bước cho thấy thuật toán đã hoạt động hiệu quả bằng cách sử dụng kết hợp AND và OR trong tìm kiếm, phù hợp với bài toán có cấu trúc rẽ nhánh và cần đánh giá nhiều khả năng kế tiếp. Bên cạnh đó nhờ việc sử dụng visited giúp tránh trạng thái đã thăm, giảm thiểu lặp vô hạn và tăng hiệu quả tìm kiếm. Đồng thời giới hạn độ sâu để tránh lan rộng không kiểm soát
#### Searching with No Observation
- Trong bài toán này, cả trạng thái đầu và trạng thái đích đều được khởi tạo ngẫu nhiên, và thuật toán không được cung cấp bất kỳ thông tin nào về trạng thái mục tiêu trong quá trình tìm kiếm. Do không loại bỏ bất kỳ trạng thái nào trong không gian tìm kiếm, thuật toán có thể duyệt qua toàn bộ không gian trạng thái. Điều này góp phần làm tăng xác suất tìm ra lời giải, mặc dù chi phí tính toán có thể lớn.
#### Searching with Partially Observation
- Thuật toán này cũng random ra 8 trạng thái đầu nhưng khác biệt so với **Searching with No Observation** là có nhìn thấy 1 phần của trạng thái đích nên sau mỗi bước chạy các trạng thái không thỏa mãn phần thông tin nhìn thấy được sẽ bị loại bỏ dẫn đến khả năng tìm ra lời giải tương đối thấp

## V. Constraint Satisfaction Problem
### 1. Test
### 2. Backtracking
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/a02cf679-d815-4b9f-85f5-f40afd25fef0)|<p>Steps: 31</p>|
### 3. AC-3

## VI. Reinforcement Learning
### 1. Q-Learning
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
|Trạng thái bắt đầu và Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :---| :---|
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/932fff57-15c1-4738-add6-3020f35b23b8)|<p>Không tìm ra lời giải đến trạng thái đích</p>|

### 2. Algorithm Performance Comparison
#### Q-Learning
- Thuật toán Q-Learning không thể tìm ra lời giải cho game 8 Puzzle với trạng thái đã khởi tạo điều này có thể do 1 số lý do như chưa đủ số vòng lặp học (episodes). Số lượng trạng thái của game lớn nên có thể agent chưa từng đi con đường đó trong quá trình training → Q-table có thể không đủ thông tin để tìm được đường đi.


