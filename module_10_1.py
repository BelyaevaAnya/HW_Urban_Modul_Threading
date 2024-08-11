from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, mode='a', encoding='utf-8') as file:
        for word_number in range(1, word_count+1):
            file.write(f'Какое-то слово № {word_number}\n')
            sleep(0.01)

time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f'Время выполнения вызванных функций {time_end-time_start}')

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt' ))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt' ))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt' ))

time_start = datetime.now()
thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
time_end = datetime.now()
print(f'Время выполнения вызванных функций в потоках {time_end-time_start}')
# Время выполнения вызванных функций 0:00:03.497739
# Время выполнения вызванных функций в потоках 0:00:02.051499