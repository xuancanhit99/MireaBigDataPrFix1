n = int(input())
a = []
# Инициализируйте список,
# чтобы получить каждый элемент матрицы (строка за строкой)
for i in range(n):
    a += [int(j) for j in input().split()]
print(a)
