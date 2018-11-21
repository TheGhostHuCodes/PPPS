import threading

SHARED_RESOURCE_WITH_LOCK = 0
SHARED_RESOURCE_WITHOUT_LOCK = 0
COUNT = 1000000
SHARED_RESOURCE_LOCK = threading.Lock()


def increment_with_lock() -> None:
    global SHARED_RESOURCE_WITH_LOCK
    for _ in range(COUNT):
        SHARED_RESOURCE_LOCK.acquire()
        SHARED_RESOURCE_WITH_LOCK += 1
        SHARED_RESOURCE_LOCK.release()


def decrement_with_lock() -> None:
    global SHARED_RESOURCE_WITH_LOCK
    for _ in range(COUNT):
        SHARED_RESOURCE_LOCK.acquire()
        SHARED_RESOURCE_WITH_LOCK -= 1
        SHARED_RESOURCE_LOCK.release()


def increment_without_lock() -> None:
    global SHARED_RESOURCE_WITHOUT_LOCK
    for _ in range(COUNT):
        SHARED_RESOURCE_WITHOUT_LOCK += 1


def decrement_without_lock() -> None:
    global SHARED_RESOURCE_WITHOUT_LOCK
    for _ in range(COUNT):
        SHARED_RESOURCE_WITHOUT_LOCK -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("The value of shared variable with lock management is %s" %
          SHARED_RESOURCE_WITH_LOCK)
    print("The value of shared variable with race condition is %s" %
          SHARED_RESOURCE_WITHOUT_LOCK)