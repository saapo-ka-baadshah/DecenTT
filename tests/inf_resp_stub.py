import sys
from subprocess import PIPE, Popen
from threading import Thread
from queue import Queue, Empty

ON_POSIX = 'posix' in sys.builtin_module_names


def enqueue_output(out, queue):
    print(out)
    # for line in iter(out.readline, b''):
    #     print(line)
    out.close()


# p = Popen(["curl", "-X", "POST", "http://127.0.0.1:5001/api/v0/pubsub/sub?arg=abc"], stdout=PIPE)
p = Popen(["ipfs", "pubsub", "sub", "abc"], stdout=PIPE)
q = Queue()
t = Thread(target=enqueue_output, args=(p.stdout, q))
t.daemon = True  # thread dies with the program
t.start()

try:
    line = q.get_nowait()  # or q.get(timeout=.1)
    print(line)
except Empty:
    print('no output yet')
