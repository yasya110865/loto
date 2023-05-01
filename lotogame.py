import lotomult as loto
import random


#выбираем количество и тип игроков
num_players = int(input('Сколько будет игроков? '))
players = []
names = []
cards = []
failed = []
print('1. Человек')
print('2. Компьютер')
for i in range(num_players):
    choice = input('Выберите тип игрока: ')
    if choice == '1':
        player = loto.Person()
    elif choice == '2':
        player = loto.Computer()
    name = input('Имя игрока: ')
    players.append(player)
    names.append(name)

    #формирование  карты
    card = loto.create_card()
    cards.append(card)

#мешок с бочонками
bag = random.sample(list(range(1, 91)), 90)

while True:
    #случайный бочонок
    n = random.choice(bag)

    #убираем из мешка
    bag.remove(n)
    print(f'Новый бочонок {n}, осталось {len(bag)}')

    #печатаем карточки игрокам
    for i in range(num_players):
        if players[i] not in failed:
        # card = create_card()
            print(f'Карта игрока {names[i]},число {n} ')
            loto.print_card(cards[i])
            if isinstance(players[i], loto.Computer):
                players[i].delete(n, cards[i])
            else:
                action = input('будем зачеркивать? (y/n) ')
                if action == 'y' and n in cards[i][0] or n in cards[i][1] or n in cards[i][2]:
                    players[i].delete(n, cards[i])

                # если неправильный выбор - проигрыш, конец игры
                elif action == 'y' and n not in cards[i][0] and n not in cards[i][1] and n not in cards[i][2] \
                        or action == 'n' and n in cards[i][0] or n in cards[i][1] or n in cards[i][2]:

                    print(f'Игрок {names[i]} проиграл!')
                    failed.append(players[i])


            print(len(set(cards[i][0] + cards[i][1] + cards[i][2])))
    if (len(set(cards[i][0] + cards[i][1] + cards[i][2]))) < 3:
        print(f'Игра окончена! Победил игрок {names[i]}')
        break





