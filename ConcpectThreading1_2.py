from threading import Thread
from datetime import datetime
import requests

time_start = datetime.now()
THE_URL = 'https://api.github.com/user'
res = []
def func(url):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)

thr_1 = Thread(target=func, args=(THE_URL, ))
thr_2 = Thread(target=func, args=(THE_URL, ))
thr_3 = Thread(target=func, args=(THE_URL, ))
thr_4 = Thread(target=func, args=(THE_URL, ))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
print()
print(f'Время выполнения программы {time_end-time_start}')
print(res)
# Время выполнения программы 0:00:00.176597