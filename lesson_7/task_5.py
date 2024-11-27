# задача 5
'''
Используя map() и reduce() посчитать площадь
квартиры, имея на входе характеристики комнат квартиры.
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]
'''

from functools import reduce


def square_home(i): #
    s = i["length"] * i["width"]
    print(f'S({i["name"]}) = {s}m2')
    return s


rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

s_1 = map(square_home, rooms)
s_2 = reduce(lambda x, y: x + y, s_1)
print(f'Общая площадь квартиры = {s_2}m2')
