import multiprocessing


def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)
    output_pipe.close()


def multiply_items(pipe1, pipe2):
    closer, input_pipe = pipe1
    closer.close()
    output_pipe, _ = pipe2
    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()


if __name__ == '__main__':
    pipe1 = multiprocessing.Pipe(True)
    process_pipe1 = multiprocessing.Process(
        target=create_items, args=(pipe1, ))
    process_pipe1.start()

    pipe2 = multiprocessing.Pipe(True)
    process_pipe2 = multiprocessing.Process(
        target=multiply_items, args=(
            pipe1,
            pipe2,
        ))
    process_pipe2.start()

    pipe1[0].close()
    pipe2[0].close()

    try:
        while True:
            print(pipe2[1].recv())
    except EOFError:
        print("End")
