import random

class Card:

    def create_card(self):
        num = list(range(1, 91))
        card = []
        for i in range(3):
            numbers = sorted(random.sample(num, 9))
            idx = random.sample(range(0, 8), 4)
            for i in idx:
                numbers[i] = ' '
            num = list(set(num) - set(numbers))

            card.append(numbers)
        return card

    def __str__(self):
        return f'{card[0]}\n {card[1]}\n{card[2]}'


    def change_num(self,n,card):
        for i in range(3):
            if n in card[i]:
                card[i][card[i].index(n)] = '-'


class Person:
    '''
    игрок
    '''
    def __init__(self):

        self.name = None
        card = Card()
        self.card = card.create_card()
    def __str__(self):
        return f'{self.name}, счет игрока {self.count}'
    def __eq__(self, other):
        return self.step == other.step

    def print_card(self):
        print('-' * 23)
        print(' '.join(map(str, self.card[0])))
        print(' '.join(map(str, self.card[1])))
        print(' '.join(map(str, self.card[2])))
        print('-' * 23)
    def change_num(self,n):
        for i in range(3):
            if n in self.card[i]:
                self.card[i][self.card[i].index(n)] = '-'
    def __len__(self):
        return len(set(self.card[0] + self.card[1] + self.card[2]))

    def step(self, n):
        '''
        зачеркивание числа, совпадающего с заданным
        :param n: заданное число

        :return:
        '''
        self.print_card()
        if len(self) <= 3:
            res = False
        else:
            action = input('Будем зачеркивать? (y/n')
        while action not in 'YyNn':
            print('Введено неправильное значение')
            action = input('Будем зачеркивать? (y/n')


        if action == 'y' and any(n in sl for sl in self.card):
            res = True
            self.change_num(n)

        elif action == 'n' and not any(n in sl for sl in self.card):
            res = True
        elif len(self) <= 3:
            res = 'Finish'
        else:
            res = False
        return res
class Computer(Person):
    def step(self, n):
        self.print_card()
        if len(self) <= 3:
            res = 'Finish'
        else:

            res = True
        self.change_num(n)
        return res

class Game:
    def __init__(self):
        self.players = []
        self.bag = random.sample(list(range(1, 91)), 90)
        self.result = None
    def __str__(self):
        return f'количество игроков: {len(self.players)}, результат: {self.result}'

    def get_random_num(self):
        # случайный бочонок
        n = random.choice(self.bag)

        # убираем из мешка
        self.bag.remove(n)
        return n


    def game_start(self):
        self.num_players = int(input('Сколько будет игроков? '))
        print('1. Человек')
        print('2. Компьютер')
        for i in range(self.num_players):
            choice = input('Выберите тип игрока: ')
            while choice not in '12':
                print('Введено неверное значение')
                choice = input('Выберите тип игрока: ')

            if choice == '1':
                player = Person()
            elif choice == '2':
                player = Computer()
            player.name = input('Имя игрока: ')
            self.players.append(player)

    def game_play(self):
        self.game_start()
        self.result = True
        failed = []
        while  self.result == True:
            # случайный бочонок
            n = self.get_random_num()

            print(f'Новый бочонок {n}, осталось {len(self.bag)}')

            # печатаем карточки игрокам

            for player in self.players:
                if player not in failed and (len(self.players) - len(failed)) > 1:
                    print(f'Карта игрока {player.name}, число {n}')
                    self.result = player.step(n)
                    print(self.result)
                #
                    if self.result == False:
                            print(f'Игрок {player.name} проиграл!')
                            failed.append(player)

                    elif self.result == 'Finish':
                            print(f'Игра окончена выиграл игрок {player.name}')
                            print(game)
                            break

if __name__ == '__main__':
    player1 = Computer()
    player1.name = 'Max'
    player2 = Person()
    player2.name = 'Max'
    print(player1 == player2)
    # player.print_card()
    # print(player)
    # result = player.step(125)
    # print(result)
    # print(len(player))
    game = Game()
    print(game)
    game.game_play()
    print(game)

