import random

class Card:
    def __init__(self):
        # self.row = self.create_row()
        self.card = self.create_card()

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

        for i in range(3):
            row, num = self.create_row()
            card.append(row)
        # self.my_card = card
        return card
    def print_card(self):
        print('-' * 23)
        print(' '.join(map(str, self.card[0])))
        print(' '.join(map(str, self.card[1])))
        print(' '.join(map(str, self.card[2])))
        print('-' * 23)


class Person:
    '''
    игрок
    '''
    def __init__(self):
        self.count = 0
        self.name = 'Name'
        card = Card()
        self.card = card.create_card()
    # def create_row(self):
    #     num = list(range(1, 91))
    #     numbers = sorted(random.sample(num,9))
    #     idx = random.sample(range(0, 8), 4)
    #     for i in idx:
    #         numbers[i] = ' '
    #     num = list(set(num) - set(numbers))
    #     return numbers, num
    #
    # def create_card(self):
    #     card = []
    #
    #     for i in range(3):
    #         row, num = self.create_row()
    #         card.append(row)
    #     self.my_card = card
    #     return card
    # def print_card(self):
    #     print('-' * 23)
    #     print(' '.join(map(str, self.my_card[0])))
    #     print(' '.join(map(str, self.my_card[1])))
    #     print(' '.join(map(str, self.my_card[2])))
    #     print('-' * 23)


    def delete(self,n,actions):
        '''
        зачеркивание числа, совпадающего с заданным
        :param n: заданное число
        :param card: списки чисел с карточки
        :return:
        '''
        # card = self.my_card
        if actions == 'y' and any(n in sl for sl in self.card):
            res = 0
            for i in range(3):
                if n in self.card[i]:
                    self.card[i][self.card[i].index(n)] = '-'
                    self.count += 1




        elif actions == 'n' and not any(n in sl for sl in self.card):
            res = 0
        else:
            res = 1
        return res
class Computer(Person):

    def delete(self, n, actions = None):

        for i in range(3):
            if n in self.card[i]:
                self.card[i][self.card[i].index(n)] = '-'
                self.count += 1

            else:
                pass


class Game:
    def __init__(self):
        self.players = []
        self.failed = []
        self.names = []
        self.bag = random.sample(list(range(1, 91)), 90)

    def game_start(self):
        self.num_players = int(input('Сколько будет игроков? '))
        print('1. Человек')
        print('2. Компьютер')
        for i in range(self.num_players):
            choice = input('Выберите тип игрока: ')
            if choice == '1':
                player = Person()
            elif choice == '2':
                player = Computer()
            name = input('Имя игрока: ')
            self.players.append(player)
            self.names.append(name)
        while True:
            # случайный бочонок
            n = random.choice(self.bag)

            # убираем из мешка
            self.bag.remove(n)
            print(f'Новый бочонок {n}, осталось {len(self.bag)}')

            # печатаем карточки игрокам
            for i in range(self.num_players):
                # если игрок еще в игре
                if self.players[i] not in self.failed:

                    print(f'Карта игрока {self.names[i]},число {n} ')
                    # card = self.players[i].create_card()
                    self.players[i].card.print_card()
                    if isinstance(self.players[i], Computer):
                        self.players[i].delete(n)

                    else:
                        action = input('будем зачеркивать? (y/n) ')
                        res = self.players[i].delete(n,  action)
                        if res == 1:
                            print(f'Игрок {self.names[i]} проиграл!')
                            self.failed.append(self.players[i])
                        print(f'Счет игрока {self.players[i].count}')

            # if len(self.failed) == num_players:
            #     print('Игра окончена!')
            #     break
                # print(len(set(cards[i][0] + cards[i][1] + cards[i][2])))
            if (len(set(self.players[i].card[0] + self.players[i].card[1] + self.players[i].card[2]))) < 3:
                print(f'Игра окончена! Победил игрок {self.names[i]}')
                break
            if len(self.failed) == self.num_players:
                print('Игра окончена!')
                break



if __name__ == '__main__':
    pass