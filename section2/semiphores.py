import threading
import time
import random

SEMAPHORE = threading.Semaphore(0)
ITEM = None


def consumer() -> None:
    global ITEM
    print("Consumer is waiting.")
    SEMAPHORE.acquire()
    print("Consumer notify: consumed item number %s" % ITEM)


def producer() -> None:
    global ITEM
    time.sleep(2)
    ITEM = random.randint(0, 1000)
    print("Producer notify: produced item number %s" % ITEM)
    SEMAPHORE.release()


if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()

        t1.join()
        t2.join()
    print("Program terminated")
