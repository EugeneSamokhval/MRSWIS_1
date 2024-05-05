# Лабораторная работа 1 по дисциплине МРЗвИС
# Выполнена студентами группы 121703
# БГУИР Самохвал Е.С., Шурмель К.А.
# Вариант 2 - алгоритм вычисления произведения пары 4-разрядных чисел
# умножением с младщих разрядов со сдвигом частичной суммы вправо;
# 06.03.2023

from multiprocessing import Process, Pipe
from prettytable import PrettyTable
import machineoperations as mo
import consts
import copy
import datetime
import logging

tic_counter = 0
logger = logging.getLogger(__name__)
logging.basicConfig(filename='log.log', level=logging.INFO)


class DataContainer:
    def __init__(self, data, index, multiplier, current_number, multiplicant) -> None:
        self.data = data
        self.index = index
        self.current_number = current_number
        self.multiplier = multiplier
        self.multiplicant = multiplicant


def worker_shift(conn1, conn2):
    logger.info('shift is started')
    while True:
        # try:
        data = conn1.recv()
        logging.info(str(data.data) + ' Processing following object started:' + str(data.current_number) + '  ' + str(data.index) + ' ' +
                     datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        data: DataContainer
        result = copy.copy(data)
        result.data = mo.shear_right(data.data, 1)
        logging.info(str(result.data) + ' Processing following object complete:' + str(
            data.current_number) + '  ' + str(data.index) + ' ' + datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        conn2.send(result)
        # except:
        #     logger.error('Error during processing:', data,
        #                  datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))


def worker_sum(conn1, conn2):
    logger.info('sum is started')
    while True:
        # try:
        data = conn1.recv()
        data: DataContainer
        result = copy.copy(data)
        logging.info(str(data.data) + ' Processing following object started:' + str(data.current_number) + '  ' + str(data.index) + ' ' +
                     datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        if data.multiplier[data.index]:
            result.data = mo.machine_sum(
                data.data, data.multiplicant)
        result.index += 1
        logging.info(str(result.data) + 'Processing following object complete:' + str(data.current_number) + '  ' + str(data.index) + ' ' +
                     datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        conn2.send(result)
        # except:
        #     logger.error('Error during processing:', data,
        #                  datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))


def pipeline(vector_1, vector_2, logger):
    result = []
    connections = [Pipe() for _ in range(8)]
    processes = [
        Process(target=worker_sum, args=(
            connections[0][1], connections[1][0])),
        Process(target=worker_shift, args=(
            connections[1][1], connections[2][0])),
        Process(target=worker_sum, args=(
            connections[2][1], connections[3][0])),
        Process(target=worker_shift, args=(
            connections[3][1], connections[4][0])),
        Process(target=worker_sum, args=(
            connections[4][1], connections[5][0])),
        Process(target=worker_shift, args=(
            connections[5][1], connections[6][0])),
        Process(target=worker_sum, args=(
            connections[6][1], connections[7][0]))]
    for p in processes:
        p.start()
    for index in range(len(vector_1)):
        reversed_multiplier = vector_2[index]
        reversed_multiplier.reverse()
        entry_data = DataContainer(
            current_number=index, multiplier=reversed_multiplier, data=mo.create_array(consts.NUMSIZE), index=0, multiplicant=mo.shear_left(
                vector_1[index], int(consts.NUMSIZE/2)-1))
        connections[0][0].send(entry_data)
    while len(result) < len(vector_1):
        item = connections[-1][0].recv()
        logger.info(f'Result {item.current_number} gathered' + ' ' +
                    datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        result.append(connections[-1][1].recv())
    for p in processes:
        p.join()

    # pipe_data_collector = []
    # for index in range(len(vector_1)):
    #     tic_counter = index
    #     temp_result = [mo.create_array(consts.NUMSIZE)]
    #     vector_1[index] = mo.shear_left(
    #         vector_1[index], int(consts.NUMSIZE/2)-1)
    #     vector_2[index].reverse()
    #     for subindex in range(0, int(consts.NUMSIZE/2)):
    #         if vector_2[index][subindex]:
    #             temp_result.append(mo.machine_sum(
    #                 temp_result[len(temp_result)-1], vector_1[index]))
    #             pipe_data_collector.append([tic_counter, 'sum', temp_result[len(
    #                 temp_result)-2], vector_1[index], temp_result[len(temp_result)-1], index])
    #             tic_counter += 1
    #         else:
    #             pipe_data_collector.append([tic_counter, 'sum', temp_result[len(
    #                 temp_result)-2], mo.create_array(consts.NUMSIZE), temp_result[len(temp_result)-1], index])
    #         temp_result.append(mo.shear_right(
    #             temp_result[len(temp_result)-1], 1))
    #         pipe_data_collector.append(
    #             [tic_counter, 'shearr', temp_result[len(temp_result)-2], 1, temp_result[len(temp_result)-1], index])
    #         tic_counter += 1
    #     temp_result.pop(-1)
    #     result.append(temp_result)
    #     pipe_data_collector.pop(-1)
    # pipe_data_collector.sort(key=lambda x: x[0])
    # pipeview(pipe_data_collector, len(vector_1))
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
