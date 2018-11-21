import threading
import time


class Box:
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n: int) -> None:
        with Box.lock:
            self.total_items += n

    def add(self):
        with Box.lock:
            self.execute(1)

    def remove(self):
        with Box.lock:
            self.execute(-1)


def adder(box: Box, items: int):
    while items > 0:
        print("Adding 1 item to the box\n")
        box.add()
        time.sleep(5)
        items -= 1


def remover(box: Box, items: int):
    while items > 0:
        print("Removing 1 item from the box\n")
        box.remove()
        time.sleep(5)
        items -= 1


if __name__ == '__main__':
    items = 5
    print("Putting %s items in the box " % items)
    box = Box()
    t1 = threading.Thread(target=adder, args=(box, items))
    t2 = threading.Thread(target=remover, args=(box, items))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("%s items still remain in the box" % box.total_items)