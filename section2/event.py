import random
from threading import Thread, Event
from typing import List
import time

ITEMS = []
EVENT = Event()


class consumer(Thread):
    def __init__(self, items: List[int], event: Event):
        super().__init__()
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait(timeout=5)
            try:
                item = self.items.pop()
                print("Consumer notify: %d popped from list %s" % (item,
                                                                   self.name))
            except IndexError:
                print("Consumer notify: out of items, exiting")
                break


class producer(Thread):
    def __init__(self, items: List[int], event: Event):
        super().__init__()
        self.items = items
        self.event = event

    def run(self):
        for _ in range(10):
            time.sleep(2)
            item = random.randint(0, 256)
            self.items.append(item)
            print("Producer notify: item %d appended to list by %s" %
                  (item, self.name))
            self.event.set()
            print("Producer notify: event set by %s" % self.name)
            self.event.clear()
            print("Producer notify: event cleared by %s\n" % self.name)


if __name__ == '__main__':
    t1 = producer(ITEMS, EVENT)
    t2 = consumer(ITEMS, EVENT)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
