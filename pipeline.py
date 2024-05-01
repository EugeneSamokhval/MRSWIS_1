# Лабораторная работа 1 по дисциплине МРЗвИС
# Выполнена студентами группы 121703
# БГУИР Самохвал Е.С., Шурмель К.А.
# Вариант 2 - алгоритм вычисления произведения пары 4-разрядных чисел
# умножением с младщих разрядов со сдвигом частичной суммы вправо;
# 06.03.2023

import machineoperations as mo
import consts
from prettytable import PrettyTable


def pipeline(vector_1, vector_2):
    result = []
    pipe_data_collector = []
    for index in range(len(vector_1)):
        tic_counter = index
        temp_result = [mo.create_array(consts.NUMSIZE)]
        vector_1[index] = mo.shear_left(
            vector_1[index], int(consts.NUMSIZE/2)-1)
        vector_2[index].reverse()
        for subindex in range(0, int(consts.NUMSIZE/2)):
            if vector_2[index][subindex]:
                temp_result.append(mo.machine_sum(
                    temp_result[len(temp_result)-1], vector_1[index]))
                pipe_data_collector.append([tic_counter, 'sum', temp_result[len(
                    temp_result)-2], vector_1[index], temp_result[len(temp_result)-1], index])
                tic_counter += 1
            else:
                pipe_data_collector.append([tic_counter, 'sum', temp_result[len(
                    temp_result)-2], mo.create_array(consts.NUMSIZE), temp_result[len(temp_result)-1], index])
            temp_result.append(mo.shear_right(
                temp_result[len(temp_result)-1], 1))
            pipe_data_collector.append(
                [tic_counter, 'shearr', temp_result[len(temp_result)-2], 1, temp_result[len(temp_result)-1], index])
            tic_counter += 1
        temp_result.pop(-1)
        result.append(temp_result)
        pipe_data_collector.pop(-1)
    pipe_data_collector.sort(key=lambda x: x[0])
    pipeview(pipe_data_collector, len(vector_1))
    return result


def pipeview(content: list, vectors_len):
    numbers = [[] for entry in range(vectors_len)]
    table_array = [[] for index in range(len(numbers))]
    for index in range(len(content)):
        numbers[content[index][-1]].append(content[index])
    step = 0
    for index in range(len(numbers)):
        table_array[index] = [None for i in range(step)]
        for subindex in range(len(numbers[index])):
            table_array[index].append(numbers[index][subindex])
        step += 1
    maximal_len = max([len(entry) for entry in table_array])
    for index in range(len(table_array)):
        while len(table_array[index]) < maximal_len:
            table_array[index].append(None)
    for subindex in range(maximal_len):
        print(200*'-', "\nТакт ", subindex, '\n')
        for index in range(len(table_array)):
            entry = table_array[index][subindex]
            if not entry:
                print('Ожидает очереди')
            elif entry[1] == 'sum':
                stage = subindex - entry[-1]
                print('Этап ', stage)
                print('Суммирование чисел: ',
                      entry[2], '+', entry[3], '=', entry[4])
            elif entry[1] == 'shearl':
                stage = subindex - entry[-1]
                print('Этап ', stage)
                print('Сдвиг влево: ', entry[2],
                      'на', entry[3], '=', entry[4])
            elif entry[1] == 'shearr':
                stage = subindex - entry[-1]
                print('Этап ', stage)
                print('Сдвиг вправо: ', entry[2],
                      'на', entry[3], '=', entry[4])
