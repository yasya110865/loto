# функция для создания карточек

import random
def create_row(num = list(range(1,91))):
    '''
    генерация ряда из 9 случайных цифр
    :param num: список для случайного выбора цифры
    :return: сгенерированный список, новый список для генерации следующего ряда
    '''

    # ряд случайных чисел
    numbers = random.sample(num, 9)

    #сортируем по порядку
    numbers = sorted(numbers)

    # генерация случайных индексов для замены на пробелы
    idx = random.sample(range(0, 8), 4)

    # замена чисел пробелами по сгенерированным индексам
    for i in idx:
        numbers[i] = ' '

    # убираем числа, попавшие в выборку, из основного списка для исключения повторов в следующем ряду
    num = list(set(num) - set(numbers))
    return numbers, num
def create_card():
    '''
    создание трех рядов уникальных цифр
    :return:
    '''
    row1, num1 = create_row()
    row2, num2 = create_row(num=num1)
    row3, num3 = create_row(num=num2)

    return row1, row2, row3

def print_card(row1,row2,row3):
    '''
    печать карточки
    :param row1: первый ряд
    :param row2: второй ряд
    :param row3: третий ряд
    :return:
    '''
    print('-'* 23)
    print(' '.join(map(str, row1)))
    print(' '.join(map(str, row2)))
    print(' '.join(map(str, row3)))
    print('-'* 23)

class Person:
    '''
    игрок
    '''
    def __init__(self):
        self.count = 0
    def delete(self,n,*lst):
        '''
        зачеркивание числа, совпадающего с заданным
        :param n: заданное число
        :param lst: списки чисел с карточки
        :return:
        '''
        for i in range(3):
            if n in lst[i]:
                lst[i][lst[i].index(n)] = '-'
                self.count += 1
            else:
                pass

class Computer:
    def __init__(self):
        self.count = 0
    def delete(self, n, *lst):
        for i in range(3):
            if n in lst[i]:
                lst[i][lst[i].index(n)] = '-'
                self.count += 1
            else:
                pass

