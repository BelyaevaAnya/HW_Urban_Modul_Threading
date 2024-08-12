# race condition
from threading import Thread, Lock
#
# x = 0
#
#
# def thread_task():
#     global x
#     for i in range(10_000_000):
#         x = x + 1
#
#
# def main():
#     global x
#     x = 0
#     t1 = Thread(target=thread_task)
#     t2 = Thread(target=thread_task)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
# print('R')
#
# for i in range(10):
#     main()
#     print(x)

# race condition solved
print('race condition')
x = 0

lock1 = Lock()
lock2 = Lock()


def thread_task():
    global x
    for i in range(10_000_000):
        with lock1:
            x = x + 1

def thread_tsk():
    global x
    for i in range(1_000_000):
        try:
            lock1.acquire()
            x = x + 1
        finally:
            lock1.release()

def main():
    global x
    x = 0
    t1 = Thread(target=thread_tsk)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main()
    print(x)