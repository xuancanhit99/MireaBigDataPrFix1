a = int(input())
# Инициализировать пустой список
m = []

# Запустите 2 цикла, чтобы добавить элементы в список
# Результатом является длина массива, взятого от 0 до a
for i in range(a):
    j = 0
    while j < i + 1:
        m.append(i + 1)
        j += 1
    if len(m) > a:
        break
m = m[0:a]
for i in m:
    print(i, end=" ")
