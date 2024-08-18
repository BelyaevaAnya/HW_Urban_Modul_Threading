from threading import Thread
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = randint(3, 10)
        sleep(wait_time)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table_ind in range(0, len(self.tables)):
                if self.tables[table_ind].guest is None:
                    self.tables[table_ind].guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {self.tables[table_ind].number}')
                    break
                else:
                    continue
            if not guest.is_alive():
                self.queue.put(guest)
                print(f'{guest.name} в очереди')



    def discuss_guests(self):
        # ф-ция поиска свободного столика
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

# =>
# Maria сел(-а) за стол номер 1
# Oleg сел(-а) за стол номер 2
# Vakhtang сел(-а) за стол номер 3
# Sergey сел(-а) за стол номер 4
# Darya сел(-а) за стол номер 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Darya покушал(-а) и ушёл(ушла)
# Стол номер 5 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 5
# Maria покушал(-а) и ушёл(ушла)
# Стол номер 1 свободен
# Vitoria вышел(-ла) из очереди и сел(-а) за стол номер 1
# Oleg покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Nikita вышел(-ла) из очереди и сел(-а) за стол номер 2
# Vakhtang покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
# Galina вышел(-ла) из очереди и сел(-а) за стол номер 3
# Sergey покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Pavel вышел(-ла) из очереди и сел(-а) за стол номер 4
# Arman покушал(-а) и ушёл(ушла)
# Стол номер 5 свободен
# Ilya вышел(-ла) из очереди и сел(-а) за стол номер 5
# Galina покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
# Alexandra вышел(-ла) из очереди и сел(-а) за стол номер 3
# Nikita покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Alexandra покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
# Vitoria покушал(-а) и ушёл(ушла)
# Стол номер 1 свободен
# Pavel покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Ilya покушал(-а) и ушёл(ушла)
# Стол номер 5 свободен