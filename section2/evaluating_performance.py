from threading import Thread
from typing import Callable


class threads_object(Thread):
    def __init__(self, func: Callable[[], None]):
        super().__init__()
        self.func = func

    def run(self) -> None:
        self.func()


class notthread_object:
    def __init__(self, func: Callable[[], None]):
        self.func = func

    def run(self) -> None:
        self.func()


def non_threaded(num_iter: str, func: Callable[[], None]) -> None:
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(notthread_object(func))
    for i in funcs:
        i.run()


def threaded(num_threads: str, func: Callable[[], None]) -> None:
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object(func))
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


def func_pass() -> None:
    pass


def func_fib() -> None:
    a, b = 0, 1
    for _ in range(10000):
        a, b = b, a + b


def func_read() -> None:
    fh = open('test.dat', 'rb')
    size = 1024
    for _ in range(1000):
        fh.read(size)


def show_result(func_name: str, results: float) -> None:
    print("%-23s %4.6f seconds" % (func_name, results))


if __name__ == '__main__':
    import sys
    from timeit import Timer

    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]
    print("Starting tests")
    funcs = ['func_pass', 'func_fib', 'func_read']
    for fn in funcs:
        print(80 * "#")
        print(f"Testing {fn}")
        print(80 * "#")
        for i in num_threads:
            t = Timer(
                "non_threaded(%s, %s)" % (i, fn),
                'from __main__ import non_threaded, {}'.format(
                    ', '.join(funcs)))
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_result("non_threaded (%s iters)" % i, best_result)

            t = Timer(
                "threaded(%s, %s)" % (i, fn),
                'from __main__ import threaded, {}'.format(', '.join(funcs)))
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_result("threaded (%s iters)" % i, best_result)

    print("Iterations complete")