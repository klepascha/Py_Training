"""
Дан класс:
    class Lock(object):
      def __init__(self):
        self.lock = False

    Сделать менеджер контекста, который может переопределить
    значение lock на True внутри блока контекста.
"""

from contextlib import contextmanager


class Lock(object):
    def __init__(self):
        self.lock = False


class Manager(Lock):
    def __enter__(self):
        self.lock = True

    def __exit__(self, *args):
        self.lock = False


d = Manager()
print(d.lock)

with d:
    print(d.lock)

print(d.lock)
print()


@contextmanager
def manager_func(user_class):
    user_class.lock = True
    yield user_class
    user_class.lock = False


s = Lock()
print(s.lock)

with manager_func(s):
    print(s.lock)

print(s.lock)
