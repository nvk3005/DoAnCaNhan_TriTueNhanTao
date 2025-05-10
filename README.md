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
- Trang Search: Áp dụng cho 2 thuật toán Searching with No Observation và Searching with Partially Observation
- Trang Steps: Hiển thị chi tiết từng bước tìm ra lời giải của thuật toán

## Cách để chạy dự án.
- clone từ github: git clone https://github.com/nvk3005/DoAnCaNhan_TriTueNhanTao.git
- Chạy file Main.py trong thư mục
## Các thuật toán được sử dụng trong dự án

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
- [III. Local Search Algorithms](#iii-local-search-algorithms)
  - [1. Simple Hill Climbing](#1-simple-hill-climbing)
  - [2. Steepest Ascent Hill Climbing](#2-steepest-ascent-hill-climbing)
  - [3. Stochastic Hill Climbing](#3-stochastic-hill-climbing)
  - [4. Simulated Annealing](#4-simulated-annealing)
  - [5. Beam Search](#5-beam-search)

## I. Uninformed Search Algorithms
### Các thành phần chính của bài toán tìm kiếm
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
## III. Local Search Algorithms
### 1. Simple Hill Climbing

### 2. Steepest Ascent Hill Climbing

### 3. Stochastic Hill Climbing

### 4. SimulatedAnnealing

### 5. Beam Search

