"""
Сделать менеджер контекста, который бы проглатывал все исключения вызванные
   в теле и писал их в консоль, пример использования:

    with no_exceptions():
      1 / 0 # => logs: ZeroDivisionError

    print('Done!') # => continues execution
"""

from contextlib import contextmanager


@contextmanager
def try_except():
    try:
        yield
        print('Continues execution')
    except Exception as e:
        print('logs: ', e)


with try_except():
    print(1/0)

with try_except():
    print('Done')
