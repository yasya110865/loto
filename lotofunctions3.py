import random

class Card:
    # def __init__(self):
    #     self.card = self.create_card()

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


class Person:
    '''
    игрок
    '''
    def __init__(self):
        self.count = 0
        self.name = 'Name'
        card = Card()
        self.card = card.create_card()

    def print_card(self):
        print('-' * 23)
        print(' '.join(map(str, self.card[0])))
        print(' '.join(map(str, self.card[1])))
        print(' '.join(map(str, self.card[2])))
        print('-' * 23)


    def delete(self,n,actions):
        '''
        зачеркивание числа, совпадающего с заданным
        :param n: заданное число
        :param actions: решение игрока (y/n)
        :return:
        '''

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

    def get_random_num(self):
        # случайный бочонок
        n = random.choice(self.bag)

        # убираем из мешка
        self.bag.remove(n)
        return n

    def game_over(self, playerscard, failed, numplayers):
        if len(set(playerscard[0] + playerscard[1] + playerscard[2])) < 3:
            result = 'Gameover_vinner'
        elif len(failed) == numplayers:
            result = 'Gameover'
        else:
            result = 'Continue'
        return result
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
            n = self.get_random_num()

            print(f'Новый бочонок {n}, осталось {len(self.bag)}')

            # печатаем карточки игрокам
            for i in range(self.num_players):
                # если игрок еще в игре
                if self.players[i] not in self.failed:

                    print(f'Карта игрока {self.names[i]},число {n} ')

                    self.players[i].print_card()
                    if isinstance(self.players[i], Computer):
                        self.players[i].delete(n)

                    else:
                        action = input('будем зачеркивать? (y/n) ')
                        res = self.players[i].delete(n,  action)
                        if res == 1:
                            print(f'Игрок {self.names[i]} проиграл!')
                            self.failed.append(self.players[i])
                        print(f'Счет игрока {self.players[i].count}')

            result = self.game_over(self.players[i].card, self.failed,self.num_players)
            if result == 'Gameover_vinner':

                print(f'Игра окончена! Победил игрок {self.names[i]}')
                break
            elif result == 'Gameover':

                print('Игра окончена!')
                break



if __name__ == '__main__':
    game = Game()
    game.game_start()











