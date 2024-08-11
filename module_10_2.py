from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!\n')
        fight_day = 0
        warriors_count = 100
        while warriors_count > 0:
            fight_day += 1
            warriors_count -= self.power
            print(f'{self.name}, сражается {fight_day} день(дня)..., осталось '
                  f'{warriors_count} воинов\n')
            sleep(1)
        print(f'{self.name} одержал победу спустя {fight_day} дней!\n')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!\n')
# =>
# Sir Lancelot, на нас напали!
#
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов
#
# Sir Galahad, на нас напали!
#
# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов
#
# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов
#
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов
#
# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов
#
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов
#
# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов
#
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов
#
# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов
#
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов
#
# Sir Galahad одержал победу спустя 5 дней!
#
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов
#
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов
#
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов
#
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов
#
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов
#
# Sir Lancelot одержал победу спустя 10 дней!
#
# Все битвы закончились!