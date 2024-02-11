#!-*-coding:utf-8-*-
from datetime import datetime
from time import sleep


def timer(foo):
    """Декоратор, чтобы засекать время."""
    def inner(*args, **kwargs):
        start_time = datetime.now()
        res = foo(*args, **kwargs)
        print(f'time: {datetime.now() - start_time}')
        return res

    return inner


@timer
def foo(n):
    for x in range(n):
        print(x)
        sleep(1)


if __name__ == '__main__':
    foo(3)
    foo(5)
