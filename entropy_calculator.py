import math
import random

m = 0  # минимальное значение (минимальное количество психологов)
M = 100  # максимальное значение

# 100-точечная выборка «число психологов»:
data = [random.randint(m, M) for _ in range(100)]

# Общее число интервалов:
k = 10

# Вычисляем ширину каждого интервала:
w = (M - m) / k

# Формируем список интервалов: [(левый, правый, центр), ...]
intervals = []
for i in range(k):
    left = m + i * w
    right = m + (i + 1) * w
    center = (left + right) / 2
    intervals.append((left, right, center))

# Подсчитываем, сколько точек попало в каждый интервал:
n = [0] * k  # массив частот
for x in data:
    for idx, (left, right, _) in enumerate(intervals):
        if idx < k - 1:
            if left <= x < right:
                n[idx] += 1
                break
        else:
            if left <= x <= right:
                n[idx] += 1
                break

# Общее число наблюдений:
N = len(data)

# Относительные частоты P_i = n_i / N
P = [count / N for count in n]

# Математическое ожидание (используем центры интервалов):
M_mean = 0.0
for (left, right, center), P_i in zip(intervals, P):
    M_mean += center * P_i

# Дисперсия
D = 0.0
for (left, right, center), P_i in zip(intervals, P):
    D += P_i * (center - M_mean) ** 2

# Стандартное отклонение
sigma = math.sqrt(D)

# Энтропия (суммируем только по P_i>0)
H = 0.0
for P_i in P:
    if P_i > 0:
        H -= P_i * math.log2(P_i)

print(f"Выборка (100 значений числа психологов):\n{data}\n")
print(f"Минимум m = {m}, Максимум M = {M}")
print(f"Число интервалов k = {k}")
print(f"Плавающая ширина интервала w = {w:.4f}\n")

header = f"{'Интервал':<15}{'Центр':>10}{'n_i':>8}{'P_i':>8}"
print(header)
print('-' * len(header))

for idx, (left, right, center) in enumerate(intervals):
    if idx < k - 1:
        interval_label = f"[{left:.1f}–{right:.1f})"
    else:
        interval_label = f"[{left:.1f}–{right:.1f}]"
    print(f"{interval_label:<15}{center:>10.2f}{n[idx]:>8}{P[idx]:>8.3f}")

print("\nРассчитанные характеристики:")
print(f"M (мат. ожидание)          = {M_mean:.4f} психологов")
print(f"D (дисперсия)              = {D:.4f} (число психологов²)")
print(f"σ (стандартное отклонение) = {sigma:.4f} психологов")
print(f"H (энтропия)               = {H:.4f} бит")
