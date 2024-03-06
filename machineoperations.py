# Лабораторная работа 1 по дисциплине МРЗвИС
# Выполнена студентами группы 121703
# БГУИР Самохвал Е.С., Шурмель К.А.
# Вариант 2 - алгоритм вычисления произведения пары 4-разрядных чисел
# умножением с младщих разрядов со сдвигом частичной суммы вправо;
# 06.03.2023

from consts import NUMSIZE


def create_array(arr_len: int, filler=0) -> list:
    return [filler for index in range(arr_len)]


def shear_left(num_1, shear_val):
    if not shear_val:
        return num_1

    result = create_array(NUMSIZE)
    for index in range(shear_val, NUMSIZE):
        result[index-shear_val] = num_1[index]
    return result


def shear_right(num_1, shear_val):
    if shear_val == 0:
        return num_1

    result = create_array(NUMSIZE)
    for index in range(0, NUMSIZE-shear_val):
        result[index + shear_val] = num_1[index]
    return result


def dec_to_bin(decimal: int):
    result = create_array(NUMSIZE)
    bin_str = bin(decimal)
    bin_str = bin_str.removeprefix('0b')
    bin_str = '0'*(8 - len(bin_str)) + bin_str

    for index in range(NUMSIZE):
        result[index] = int(bin_str[index])
    return result


def machine_and(num_1, num_2):
    if (num_2 == 1):
        return num_1
    else:
        return create_array(NUMSIZE)


def machine_sum(num_1, num_2):
    result = create_array(NUMSIZE)
    index = NUMSIZE-1
    while index >= 0:
        result[index] += num_1[index] + num_2[index]
        if result[index] > 1:
            result[index - 1] += 1
            result[index] -= 2
        index -= 1
    return result


def bin_to_dec(inpt: list):
    str_conversion = '0b' + \
        str(inpt).replace('[', '').replace(']',
                                           '').replace(',', '').replace(' ', '')
    result = int(str_conversion, 2)
    return result
