import numpy as np
import matplotlib.pyplot as plt

# 1. Создаем "Хаос": Генерируем 10,000 абсолютно случайных чисел от 0 до 100
# Это как если бы 10,000 человек выкрикивали случайные числа.
data = np.random.randint(0, 100, 10000)

# 2. Магия ЦПТ: Берем 1000 выборок по 50 чисел и считаем их среднее значение
means = [np.mean(np.random.choice(data, 50)) for _ in range(1000)]

# 3. Визуализируем результат
plt.figure(figsize=(10, 6))
plt.hist(means, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Центральная Предельная Теорема в действии")
plt.xlabel("Средние значения выборок")
plt.ylabel("Частота появления")
plt.grid(axis='y', alpha=0.3)
plt.show()