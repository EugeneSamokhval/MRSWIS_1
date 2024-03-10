# Лабораторная работа 1 по дисциплине МРЗвИС
# Выполнена студентами группы 121703
# БГУИР Самохвал Е.С., Шурмель К.А.
# Вариант 2 - алгоритм вычисления произведения пары 4-разрядных чисел
# умножением с младщих разрядов со сдвигом частичной суммы вправо;
# 06.03.2024

import validation
import machineoperations as mo
from pipeline import pipeline


def main():
    print('Конвеер')
    while (1):
        user_inpt1 = input(
            'Введите первый вектор, как показано на следующем примере: 10, 12, 13, 5, 6\n')
        user_inpt2 = input(
            'Введите второй вектор, как показано на следующем примере: 10, 12, 13, 5, 6\n')
        valid_user_inpt1, valid_user_inpt2 = validation.valdate_input(
            user_inpt1, user_inpt2)
        if not valid_user_inpt1 and not valid_user_inpt2:
            continue
        valid_user_inpt1 = [mo.dec_to_bin(dec) for dec in valid_user_inpt1]
        valid_user_inpt2 = [mo.dec_to_bin(dec) for dec in valid_user_inpt2]
        result = pipeline(valid_user_inpt1, valid_user_inpt2)
        index = 0
        for iteration in result:
            print(index, 'Результат:', mo.bin_to_dec(
                iteration[len(iteration)-1]), '   ', iteration[len(iteration)-1])
            index += 1
        if input('Продожить y/n ?') == 'n':
            break


if __name__ == '__main__':
    main()
