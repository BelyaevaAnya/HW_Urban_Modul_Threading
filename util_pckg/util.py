import datetime
import json
from random import randint
from pathlib import Path

data_folder = "./json_files/"
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']


def write_json():
    res = []
    for file in files:
        for _ in range(100_000):
            res.append(randint(0, 10000))
        with open(data_folder + file, 'w') as fl_obj:
            json.dump(res, fl_obj)
        res = []


# Функция генерации данных для файлов
write_json()

res_to_count = []
start = datetime.datetime.now()
for file in files:
    with open(data_folder + file, 'r') as fl_obj:
        data = json.load(fl_obj)
        res_to_count.extend(data)
print(sum(res_to_count))
end = datetime.datetime.now()
print(end-start)


