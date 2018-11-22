import random
import time
from threading import Thread, Event
from queue import Queue


class producer(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print("Producer notify: item %d appended to queue by %s\n" %
                  (item, self.name))
            time.sleep(1)


class consumer(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print("Consumer notify: %d popped from queue by %s" % (item,
                                                                   self.name))
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    t3 = consumer(queue)
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()