# Смена переменных.
a, b = 1, 2
a, b = b, a
print(a, b)

# Перевернуть список.
lst = [1, 2, 3]
res = lst[::-1]
print(res)

# Убрать дубли.
lst = [1, 2, 2, 3, 3, 4]
res = list(set(lst))
print(res)

# Применить функцию к каждому элементу, map
lst = ['a', 'b', 'c']
res = list(map(str.upper, lst))
print(res)

# Распаковка
lst = [1, 2, 3]
one, two, three = lst
print(one, two, three)


def print_all(*args):
    for i, x in enumerate(args):
        print(f'{i}: {x}')


lst = [1, 2, 3]
print_all(*lst)
