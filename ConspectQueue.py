from threading import Thread
import queue
from time import sleep


def producer(queue):
    """
    Кладет в очередь сообщение
    :param queue: очередь
    :return:
    """
    c = 0
    while True:
        c += 1
        message = f'ping {c}'
        # положили в очередь сообщение
        queue.put(message)


def consumer(queue):
    """
    Достает из очереди сообщение из producer(queue)
    :param queue: очередь сообщений из producer
    :return:
    """
    while True:
        message = queue.get()
        sleep(1)
        print(message)


q = queue.Queue()
tr1 = Thread(target=producer, args=(q,))
tr2 = Thread(target=consumer, args=(q,))

tr1.start()
tr2.start()

tr1.join()
tr2.join()
