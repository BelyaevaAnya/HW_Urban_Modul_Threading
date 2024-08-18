# GIL
# Global Interpretator Lock
# from threading import Thread
# import json
# x = 0
# for i in range(1000000000):
#     x += 1
#     # I/O bound

# def count_up(name, n):
#     for i in range(n):
#         print(name, n, sep=": ")
#
# t1 = Thread(target=count_up, args=('Thread #1', 5))
# t2 = Thread(target=count_up, args=('Thread #2', 5))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
import datetime
from threading import Thread
import util
import json

res = []
threads = []
dir = util.data_folder
files = ['file1.json',
         'file2.json',
         'file3.json',
         'file4.json']


def worker(file):
    with open(dir+file, 'r') as file_obj:
        js = json.load(file_obj)
        res.extend(js)


start = datetime.datetime.now()

for i in range(len(files)):
    t = Thread(target=worker, args=(files[i]))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = datetime.datetime.now()

print('Summ: ' + str(sum(res)))
print('Time: ' + str(end - start))
