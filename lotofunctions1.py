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
    card = []
    num = list(range(1, 91))
    for i in range(3):
        row, num = create_row(num=num)
        card.append(row)

    return card
def print_card(card):
    '''
    печать карточки
    :param card: список из трех рядов цифр
    '''
    print('-'* 23)
    print(' '.join(map(str, card[0])))
    print(' '.join(map(str, card[1])))
    print(' '.join(map(str, card[2])))
    print('-'* 23)

class Person:
    '''
    игрок
    '''
    def __init__(self):
        self.count = 0
    def delete(self,n,card):
        '''
        зачеркивание числа, совпадающего с заданным
        :param n: заданное число
        :param card: списки чисел с карточки
        :return:
        '''
        for i in range(3):
            if n in card[i]:
                card[i][card[i].index(n)] = '-'
                self.count += 1
class Computer:
    def __init__(self):
        self.count = 0
    def delete(self, n, card):
        for i in range(3):
            if n in card[i]:
                card[i][card[i].index(n)] = '-'
                self.count += 1

if __name__ =='__main__':
    #выбираем количество и тип игроков
    num_players = int(input('Сколько будет игроков? '))
    players = []
    names = []
    cards = []
    failed = []
    print('1. Человек')
    print('2. Компьютер')
    for i in range(num_players):
        # if players[i] not in failed:
            choice = input('Выберите тип игрока: ')
            if choice == '1':
                player = Person()
            elif choice == '2':
                player = Computer()
            name = input('Имя игрока: ')
            players.append(player)
            names.append(name)

        #формирование  карты
            card = create_card()
            cards.append(card)

    #случайный бочонок
    bag = random.sample(list(range(1, 91)), 9)

    n = random.choice(bag)

    # убираем из мешка
    bag.remove(n)
    print(f'Новый бочонок {n}, осталось {len(bag)}')


    for i in range(num_players):
        if players[i] not in failed:
        # card = create_card()
            print(f'Карта игрока {i}')
            print_card(cards[i])
            if isinstance(players[i], Computer):
                players[i].delete(n, cards[i])
            else:
                desition  = input('будем зачеркивать? (y/n) ')
                if desition == 'y':
                    action = True
                else:
                    action = False
                print(action)
                result = players[i].delete(n, cards[i], action=action)
                print(result)
                if result == False:
                    print(f'Игрок {names[i]} проиграл!')
                    failed.append(players[i])
                print(failed)
                print(players)
        # print_card(cards[i])
