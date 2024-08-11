from threading import Thread
import requests


class Getter(Thread):
    res = []

    def __init__(self, url):
        self.THE_URL = url
        super().__init__()

    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


threads = []
num_of_genres = 10

for i in range(num_of_genres):
    THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
    thread = Getter(THE_URL)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(Getter.res)
# assert len(Getter.res) == num_of_genres - 1
# Traceback (most recent call last):
#   File "C:\Users\belae\PycharmProjects\HW_Urban_Modul_Threading\ConcpectClassesThreading.py", line 30, in <module>
#     assert len(Getter.res) == num_of_genres - 1
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError
assert len(Getter.res) == num_of_genres
# ['punkfuture', 'wind EDM', 'ukulele soundtrack', 'surf kodo drum', 'necromotown',
# 'basque zither whittle', 'swedish-fox', 'italo blues in the dark', 'indie dirty south R&B',
# 'boston anarcho-a capella sextet']
