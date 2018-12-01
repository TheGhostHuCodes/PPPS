import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    time.sleep(3)
    print("Ending %s \n" % name)


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process', target=foo)
    background_process.daemon = True

    not_background_process = multiprocessing.Process(
        name='not_background_process', target=foo)
    not_background_process.daemon = False

    background_process.start()
    not_background_process.start()
