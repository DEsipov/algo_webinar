#!-*-coding:utf-8-*-

"""
Найти заданное число в списке.
"""
import unittest


def recursion_print(lst, index=0):
    if index >= len(lst):
        return

    print(f'index:  {index}: lst[index]: {lst[index]}')
    recursion_print(lst, index + 1)


def recursion_sum(n):
    """Сумма чисел от 0 до n"""
    if n == 1:
        return 1

    return n + recursion_sum(n - 1)


class RecursTestCase(unittest.TestCase):
    """Тесты функции преобразования данных."""

    def test_rec_print_list(self):
        lst = 'hello'

        recursion_print(lst)

    def test_recursion_sum(self):
        res = recursion_sum(5)
        print(f'\nres: {res}, expect: {sum(range(6))}')


if __name__ == '__main__':
    unittest.main()

