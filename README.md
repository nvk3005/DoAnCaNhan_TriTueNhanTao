# Đồ Án Cá Nhân - Trí Tuệ Nhân Tạo (Artificial Intelligence)

## Giới thiệu tổng quan về dự án
Dự án được xây dựng nhằm mục đích nghiên cứu, đánh giá hiệu suất của các thuật toán thuộc các nhóm thuật toán khác nhau như Uninformed Search Algorithms, Informed Search Algorithms, Local Search Algorithms
dựa trên việc áp dụng để giải quyết một vấn đề cụ thể là giải trò chơi "8-Puzzle".
> Dự án được thực hiện bởi [Nguyễn Văn Kế - MSSV: 23110234](https://github.com/nvk3005)

## Các công nghệ dùng trong dự án
- Python 3.10+
- Matplotlib
- Qt Designer (PyQt5)

## Cách thức hoạt động của dự án
Giao diện GUI của dự án được chia làm 3 trang chính:
- Trang Input: Cho phép người dùng nhập trạng thái bắt đầu và trạng thái đích
- Trang Result: Cho phép người dùng chọn thuật toán muốn áp dụng để tìm ra lời giải cho bài toán
- Trang Steps: Hiển thị chi tiết từng bước tìm ra lời giải của thuật toán

## Các thuật toán được sử dụng trong dự án

- [I. Uninformed Search Algorithms](#i-uninformed-search-algorithms)
  - [1. Breadth-First Search](#1-breadth-first-search)
  - [2. Depth-First Search](#2-depth-first-search)
  - [3. Uniform Cost Search](#3-uniform-cost-search)
  - [4. Iterative Deepening Search](#4-iterative-deepening-search)
- [II. Informed Search Algorithms](#ii-informed-search-algorithms)
  - [1. A* Search](#1-a-search)
  - [2. Greedy Best-First Search](#2-greedy-best-first-search)
  - [3. Iterative Deepening A*](#3-iterative-deepening-a)
- [III. Local Search Algorithms](#iii-local-search-algorithms)
  - [1. Simple Hill Climbing](#1-simple-hill-climbing)
  - [2. Steepest Ascent Hill Climbing](#2-steepest-ascent-hill-climbing)
  - [3. Stochastic Hill Climbing](#3-stochastic-hill-climbing)
  - [4. Simulated Annealing](#4-simulated-annealing)
  - [5. Beam Search](#5-beam-search)

## I. Uninformed Search Algorithms
### 1. Breadth-First Search
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|![](https://github.com/user-attachments/assets/951a4c22-9f5e-4549-8311-dc0c96200e25)|<p>Steps: 23</p>|
### 2. dfs – Depth-First Search
**No Solution**
### 3. ucs – Uniform Cost Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b7a98cda-93bb-4bfe-a3c0-a370a19e980d) |<p>Time: 0.33811870007775724s</p><p>Steps: 23</p>|
### 4. ids – Iterative Deepening Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b788ce8e-82a2-43ce-a537-f029e27a5c95)|<p>Time: 0.24040450004395097s</p><p>Steps: 27</p>|

## II. Informed Search Algorithms
### 1. aStar – A* Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/03236232-9ebb-49a4-8b00-a4885c027a4a)|<p>Time: 0.010279600042849779s</p><p>Steps: 23</p>|
### 2. greedy – Greedy Best-First Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/16e8b254-43bf-45d4-972b-c76981cf251b)|<p>Time: 0.005781499901786447s</p><p>Steps: 79</p>
### 3. idaStar – Iterative Deepening A*

## III. Local Search Algorithms
### 1. SHC – Simple Hill Climbing
### 2. SAHC – Steepest Ascent Hill Climbing
### 3. StochasticHC – Stochastic Hill Climbing
### 4. SimAnn – SimulatedAnnealing
### 5. BeamSearch – Beam Search
