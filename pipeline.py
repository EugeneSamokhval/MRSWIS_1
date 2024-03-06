# Лабораторная работа 1 по дисциплине МРЗвИС
# Выполнена студентами группы 121703
# БГУИР Самохвал Е.С., Шурмель К.А.
# Вариант 2 - алгоритм вычисления произведения пары 4-разрядных чисел
# умножением с младщих разрядов со сдвигом частичной суммы вправо;
# 06.03.2023

import machineoperations as mo
import consts


def pipeline(vector_1, vector_2):
    result = []
    pipe_data_collector = []
    for index in range(len(vector_1)):
        tic_counter = index + 1
        temp_result = [mo.create_array(consts.NUMSIZE)]
        vector_1[index] = mo.shear_left(
            vector_1[index], int(consts.NUMSIZE/2)-1)
        vector_2[index].reverse()
        for subindex in range(0, int(consts.NUMSIZE/2)):
            if vector_2[index][subindex]:
                temp_result.append(mo.machine_sum(
                    temp_result[len(temp_result)-1], vector_1[index]))
                pipe_data_collector.append([tic_counter, 'sum', temp_result[len(
                    temp_result)-2], vector_1[index], temp_result[len(temp_result)-1]])
                tic_counter += 1
            temp_result.append(mo.shear_right(
                temp_result[len(temp_result)-1], 1))
            pipe_data_collector.append(
                [tic_counter, 'shearr', temp_result[len(temp_result)-2], 1, temp_result[len(temp_result)-1]])
            tic_counter += 1
        temp_result.append(mo.shear_left(temp_result[len(temp_result)-1], 1))
        pipe_data_collector.append([tic_counter, 'shearl', temp_result[len(
            temp_result)-2], 1, temp_result[len(temp_result)-1]])
        result.append(temp_result)
    pipe_data_collector.sort(key=lambda x: x[0])
    pipeview(pipe_data_collector, tic_counter)
    return result


def pipeview(content: list, tic_couter):
    for tic in range(1, tic_couter):
        print("Такт ", tic)
        for entry in content:
            if entry[0] == tic:
                if entry[1] == 'sum':
                    print('Суммирование чисел: ',
                          entry[2], '+', entry[3], '=', entry[4])
                elif entry[1] == 'shearr':
                    print('Сдвиг вправо: ', entry[2],
                          'на', entry[3], '=', entry[4])
                elif entry[1] == 'shearl':
                    print('Сдвиг влево: ', entry[2],
                          'на', entry[3], '=', entry[4])
