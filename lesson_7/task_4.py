# задача 4
'''Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
'''

import time


def timer_1(fun_1):
    def fun_2():
        start_time = time.time()  # Начало отсчёта времени
        fun_1()
        end_time = time.time()  # Конец отсчёта времени
        execution_time = end_time - start_time  # Время выполнения
        print(f"Execution Time: {execution_time} seconds")

    return fun_2


@timer_1
def some_func():
    time.sleep(0.45)


some_func()
