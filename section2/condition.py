from threading import Condition, Thread
import time

ITEMS = []
CONDITION = Condition()


class consumer(Thread):
    def __init__(self):
        super().__init__()

    def consume(self):
        global CONDITION
        global ITEMS

        with CONDITION:
            if len(ITEMS) == 0:
                print("Consumer notify: no item to consume")
                CONDITION.wait()
            ITEMS.pop()
            print("Consumer notify: consumed 1 item")
            print("Consumer notify: items to consume are " + str(len(ITEMS)))
            CONDITION.notify()

    def run(self):
        for _ in range(20):
            time.sleep(2)
            self.consume()


class producer(Thread):
    def __init__(self):
        super().__init__()

    def produce(self):
        global CONDITION
        global ITEMS

        with CONDITION:
            if len(ITEMS) == 10:
                print("Producer notify: items produced are " + str(len(ITEMS)))
                print("Producer notify: stop the production!")
                CONDITION.wait()
            ITEMS.append(1)
            print("Producer notify: total items produced " + str(len(ITEMS)))
            CONDITION.notify()

    def run(self):
        for _ in range(20):
            time.sleep(1)
            self.produce()


if __name__ == '__main__':
    producer = producer()
    consumer = consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()