import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print("Process Producer: item %d appended to queue %s" %
                  (item, self.name))
            time.sleep(1)


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        empty_count = 0
        while True:
            if empty_count > 10:
                break
            if (self.queue.empty()):
                print("The queue is empty")
                empty_count += 1
                time.sleep(2)
            else:
                item = self.queue.get()
                print("Process Consumer: item %d popped from by %s\n" %
                      (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
