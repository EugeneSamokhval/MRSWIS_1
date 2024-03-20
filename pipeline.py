# Лабораторная работа 1 по дисциплине МРЗвИС
# Выполнена студентами группы 121703
# БГУИР Самохвал Е.С., Шурмель К.А.
# Вариант 2 - алгоритм вычисления произведения пары 4-разрядных чисел
# умножением с младщих разрядов со сдвигом частичной суммы вправо;
# 06.03.2023

import machineoperations as mo
import consts
import prett


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
                pipe_data_collector.append([tic_counter, 'sum', mo.create_array(
                    consts.NUMSIZE), mo.create_array(consts.NUMSIZE), mo.create_array(consts.NUMSIZE), index])
            temp_result.append(mo.shear_right(
                temp_result[len(temp_result)-1], 1))
            pipe_data_collector.append(
                [tic_counter, 'shearr', temp_result[len(temp_result)-2], 1, temp_result[len(temp_result)-1], index])
            tic_counter += 1
        temp_result.append(mo.shear_left(temp_result[len(temp_result)-1], 1))
        pipe_data_collector.append([tic_counter, 'shearl', temp_result[len(
            temp_result)-2], 1, temp_result[len(temp_result)-1], index])
        result.append(temp_result)
    pipe_data_collector.sort(key=lambda x: x[0])
    pipeview(pipe_data_collector, tic_counter)
    return result


def pipeview(content: list, tic_counter):
    # pair = []
    # late_list = []
    # index = 0
    # tic = 0
    # while index < len(content):
    #     stage = 1
    #     if len(pair) == 0:
    #         pair.append(content[index])
    #         content.remove(content[index])
    #     elif content[index][-1] != pair[0][-1] and content[index][1] != pair[0][1]:
    #         pair.append(content[index])
    #         content.remove(content[index])
    #     else:
    #         late_list.append(content[index])
    #         index += 1
    #     if 0 < len(pair) < 2:
    #         print("\nТакт ", tic)
    #         for entry in pair:
    #             if entry[1] == 'sum':
    #                 print('Этап ', stage)
    #                 print('Суммирование чисел: ',
    #                       entry[2], '+', entry[3], '=', entry[4])
    #                 stage += 1
    #             if entry[1] == 'shearl' and entry[-1]:
    #                 print('Этап ', stage)
    #                 print('Сдвиг влево: ', entry[2],
    #                       'на', entry[3], '=', entry[4])
    #             if entry[1] == 'shearr':
    #                 print('Этап ', stage)
    #                 print('Сдвиг вправо: ', entry[2],
    #                       'на', entry[3], '=', entry[4])
    #         pair = []
    #         content = content + late_list
    #         late_list = []
    #         tic += 1
    #         index = 0
    numbers = [[] for entry in range(content[-1][-1]+1)]
    table_array = [[] for index in range(len(numbers))]
    for index in range(len(content)):
        numbers[content[index][-1]].append(content[index])
    step = 0
    for index in range(len(numbers)):
        table_array[index] = [[] for i in range(step)]
        for subindex in range(len(numbers[index])):
            table_array[index].append(numbers[subindex])
        step += 1
    print(table_array)
