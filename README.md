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
|![Image](https://github.com/user-attachments/assets/5bfa0d34-62fb-4861-8904-b045dc3567dc)|![Image](https://github.com/user-attachments/assets/0183fb1d-71cc-4646-b4dc-06685e9a9a62)|<p>Steps: 23</p>|
### 2. Depth-First Search
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)||<p>Steps: 66041</p>|
### 3. Uniform Cost Search
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)| ![Image](https://github.com/user-attachments/assets/d12d7a32-6188-437f-98a7-a17ce4d53a18)|<p>Steps: 23</p>|
### 4. Iterative Deepening Search
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)| ![Image](https://github.com/user-attachments/assets/6ca85878-596b-4800-85c1-4cdbd5f15ea3)|<p>Steps: 27</p>|
### 5. Algorithm Performance Comparison


## II. Informed Search Algorithms
### 1. A* Search
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)| ![Image](https://github.com/user-attachments/assets/dea3f349-9bca-45a0-8c83-381b536dc882)|<p>Steps: 23</p>|
### 2. Greedy Best-First Search
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|  ![Image](https://github.com/user-attachments/assets/784de3a7-df51-49c5-8bb9-bdc00887e268)|<p>Steps: 53</p>|
### 3. Iterative Deepening A*
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|  ![Image](https://github.com/user-attachments/assets/5179e356-fbc4-4e0b-9101-79f52306a621)|<p>Steps: 23</p>|
## III. Local Search Algorithms
### 1. Simple Hill Climbing
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|  Không tìm thấy lời giải|<p>Steps: 0</p>|
### 2. Steepest Ascent Hill Climbing
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|  Không tìm thấy lời giải|<p>Steps: 0</p>
### 3. Stochastic Hill Climbing
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|  Không tìm thấy lời giải|<p>Steps: 0</p>
### 4. SimulatedAnnealing
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|  Không tìm thấy lời giải|<p>Steps: 0</p>
### 5. Beam Search
|Trạng thái bắt đầu|Trạng thái đích|Lời giải|Số bước để tìm ra lời giải|
| :--- | :--- | :---| :---|
|![](https://github.com/user-attachments/assets/0b25e011-e762-43a8-bedf-9fbecfc7cd7d)|![](https://github.com/user-attachments/assets/05d09562-c4e5-4335-82db-cc6a50bf9c7e)|  ![Image](https://github.com/user-attachments/assets/77a29fc2-1ae0-4886-9782-e9295ca6cac3)|<p>Steps: 43</p>
