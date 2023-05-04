import random

class Person:
    '''
    игрок
    '''
    def __init__(self):
        self.count = 0
        self.name = 'Name'

        self.my_card = self.create_card()
    def create_row(self):
        num = list(range(1, 91))
        numbers = sorted(random.sample(num,9))
        idx = random.sample(range(0, 8), 4)
        for i in idx:
            numbers[i] = ' '
        num = list(set(num) - set(numbers))
        return numbers, num

    def create_card(self):
        card = []
        # num = list(range(1, 91))
        for i in range(3):
            row, num = self.create_row()
            card.append(row)
        self.my_card = card
        return card
    def print_card(self):
        print('-' * 23)
        print(' '.join(map(str, self.my_card[0])))
        print(' '.join(map(str, self.my_card[1])))
        print(' '.join(map(str, self.my_card[2])))
        print('-' * 23)


    def delete(self,n,card,actions):
        '''
        зачеркивание числа, совпадающего с заданным
        :param n: заданное число
        :param card: списки чисел с карточки
        :return:
        '''

        if actions == 'y' and any(n in sl for sl in card):
            res = 0
            for i in range(3):
                if n in card[i]:
                    card[i][card[i].index(n)] = '-'
                    self.count += 1




        elif actions == 'n' and not any(n in sl for sl in card):
            res = 0
        else:
            res = 1
        return res
class Computer(Person):
    def delete(self, n, card):
        for i in range(3):
            if n in card[i]:
                card[i][card[i].index(n)] = '-'
                self.count += 1
                res = 0
            else:
                res = 1
        return res


if __name__ == '__main__':

    # numbers, num = card.create_row()
    # print(numbers)
    # card.create_card()
    # print(len(card.my_card[0]))
    # my_card = card.create_card()
    player = Computer()
    print(player.name)
    # print(player.create_card())
    print(player.my_card)
    player.print_card()
    # card = Card.create_card()
    # print(card)

    # n = 5
    # player.print_card()
    # actions = 'y'
    # n = player.my_card[0][6]
    # res = player.delete(n, player.my_card, actions)
    # print(res)
    # print(player.my_card)
    print(player.name)
    print()





# def create_row(num = list(range(1,91))):
#     '''
#     генерация ряда из 9 случайных цифр
#     :param num: список для случайного выбора цифры
#     :return: сгенерированный список, новый список для генерации следующего ряда
#     '''
#
#     # ряд случайных чисел
#     numbers = random.sample(num, 9)
#
#     #сортируем по порядку
#     numbers = sorted(numbers)
#
#     # генерация случайных индексов для замены на пробелы
#     idx = random.sample(range(0, 8), 4)
#
#     # замена чисел пробелами по сгенерированным индексам
#     for i in idx:
#         numbers[i] = ' '
#
#     # убираем числа, попавшие в выборку, из основного списка для исключения повторов в следующем ряду
#     num = list(set(num) - set(numbers))
#     return numbers, num
# def create_card():
#     '''
#     создание трех рядов уникальных цифр
#     :return:
#     '''
#     card = []
#     num = list(range(1, 91))
#     for i in range(3):
#         row, num = create_row(num=num)
#         card.append(row)
#
#     return card
# def print_card(card):
#     '''
#     печать карточки
#     :param card: список из трех рядов цифр
#     '''
#     print('-'* 23)
#     print(' '.join(map(str, card[0])))
#     print(' '.join(map(str, card[1])))
#     print(' '.join(map(str, card[2])))
#     print('-'* 23)