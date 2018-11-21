import threading
import time


def first_function() -> None:
    print(threading.current_thread().getName() + str(' is Starting\n'))
    time.sleep(2)
    print(threading.current_thread().getName() + str(' is Exiting\n'))


def second_function() -> None:
    print(threading.current_thread().getName() + str(' is Starting\n'))
    time.sleep(2)
    print(threading.current_thread().getName() + str(' is Exiting\n'))


def third_function() -> None:
    print(threading.current_thread().getName() + str(' is Starting\n'))
    time.sleep(2)
    print(threading.current_thread().getName() + str(' is Exiting\n'))


if __name__ == '__main__':
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=second_function)
    t3 = threading.Thread(name='third_function', target=third_function)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()