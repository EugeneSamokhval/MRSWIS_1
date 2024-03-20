# Лабораторная работа 1 по дисциплине МРЗвИС
# Выполнена студентами группы 121703
# БГУИР Самохвал Е.С., Шурмель К.А.
# Вариант 2 - алгоритм вычисления произведения пары 4-разрядных чисел
# умножением с младщих разрядов со сдвигом частичной суммы вправо;
# 06.03.2023


def check_on_unknown(usinput: str):
    for symbol in usinput:
        symbol: str
        if not symbol.isdigit() and not symbol == ',':
            print('Неизвестный символ: ', symbol)
            return 0
    return 1


def check_on_overflow(input: list):
    for digit in input:
        if digit > 15:
            print('Число подаваемое на конвеер больше 15')
            return 0
    return 1


def valdate_input(input1: str, input2: str) -> bool:
    input1 = input1.replace(' ', '')
    input2 = input2.replace(' ', '')
    if not (check_on_unknown(input1) and check_on_unknown(input2)):
        return None, None
    input1 = input1.split(',')
    input2 = input2.split(',')
    if len(input1) != len(input2):
        print('Векторы разной длины')
        return None, None
    input1 = [int(digit) for digit in input1]
    input2 = [int(digit) for digit in input2]
    if not (check_on_overflow(input1) and check_on_overflow(input2)):
        return None, None
    print(('(' + str(input1).strip('[').strip(']')+')'))
    print(('(' + str(input2).strip('[').strip(']')+')'), '\n')
    return input1, input2
