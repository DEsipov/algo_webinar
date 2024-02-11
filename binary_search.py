#!-*-coding:utf-8-*-

"""
Найти заданное число в списке.
"""
import unittest


def binary_search(lst, target):
    sort_lst = sorted(lst)
    left = 0
    right = len(sort_lst) - 1

    while left <= right:
        center = (left + right) // 2
        if target == sort_lst[center]:
            return center

        if target > sort_lst[center]:
            left = center + 1
        else:
            right = center - 1

    return -1


class BinarySearchTestCase(unittest.TestCase):
    """Класс для тестирования функции binary_search."""

    def test_one(self):
        print('start test_one')
        lst, target = [1, 2, 3, 4], 3

        res = binary_search(lst, target)

        self.assertEqual(res, 2)

    def test_two(self):
        print('start test_two')
        lst, target = [11, -4, 1, 2, 3, 4], 4

        res = binary_search(lst, target)

        self.assertEqual(res, 4)

    def test_three(self):
        print('\nstart test_three')
        lst, target = [20, 24, 2, 11], 88

        res = binary_search(lst, target)

        self.assertEqual(res, -1)


# Триггер для запуска тестов
TEST = True

if __name__ == '__main__':
    if TEST:
        # Запуск тестов.
        unittest.main()
    else:
        # Боевой режим
        input_lst = input().split()
        input_target = input()

        result = binary_search(input_lst, input_target)
        print(result)


