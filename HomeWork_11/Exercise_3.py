"""
Сделать менеджер контекста, который бы мог измерять время выполнения блока кода,
   пример использования:

    with TimeIt() as t:
      some_long_function()

    print('Execution time was:', t.time)
"""

from contextlib import contextmanager
from time import time, sleep


@contextmanager
def timer():
    start_time = time()
    yield
    end_time = time()
    print('Execution time was: ', end_time - start_time)


def some_long_func():
    sleep(5)


with timer():
    some_long_func()
