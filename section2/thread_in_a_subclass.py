import threading
import time

EXIT_FLAG = False


class MyThread(threading.Thread):
    def __init__(self, thread_id: int, name: str, delay: int):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name + "\n")
        print_time(self, 5)
        print("Exiting " + self.name + "\n")


def print_time(thread: MyThread, counter: int):
    while counter:
        if EXIT_FLAG:
            break
        time.sleep(thread.delay)
        print("%s: %s" % (thread.name, time.ctime(time.time())))
        counter -= 1


if __name__ == '__main__':
    thread1 = MyThread(1, 'thread-1', 1)
    thread2 = MyThread(2, 'thread-2', 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exiting main thread")