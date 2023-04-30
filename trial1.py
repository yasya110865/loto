import random
import lotofunctions as loto

#создание карточек для игроков
row1, row2, row3 = loto.create_card()
row4, row5, row6 = loto.create_card()

# игроки
person = loto.Person()
comp = loto.Computer()

#мешок с бочонками
bag = random.sample(list(range(1, 91)), 90)

while True:
    #случайный бочонок
    n = random.choice(bag)

    #убираем из мешка
    bag.remove(n)
    print(f'Новый бочонок {n}, осталось {len(bag)}')

    #печатаем карточки игрокам
    print('Ваша карточка')
    loto.print_card(row1, row2, row3)
    print('Карточка компьютера')
    loto.print_card(row4, row5, row6)

    #компьютер всегда зачеркивает число, если оно есть
    comp.delete(n, row4, row5, row6)

    #игрока спрашиваем что выбрать
    action = input('Вычеркиваем? (y/n) ')

    #если число есть и выбор - зачеркнуть, то зачеркиваем
    if action == 'y' and  n in row1 or n in row2 or n in row3:
        person.delete(n, row1,row2,row3)

    #если неправильный выбор - проигрыш, конец игры
    elif action == 'y' and n not in row1 and n not in row2 and n not in row3\
            or action == 'n' and n in row1 or n in row2 or n in row3:
        print('Вы проиграли!')
        break
    #печатаем промежуточные результаты
    print(f'Счет компьютера: {comp.count}, счет игрока: {person.count}')

    #если в карточке игрока остались только черточки и пробелы, выигрыш
    if len(set(row1 + row2 + row3)) < 3:
        print('Вы выиграли!')
        break

    #если у компьютера остались только черточки и пробелы - игрок проиграл
    elif len(set(row4 + row5 + row6)) < 3:
        print('Вы проиграли!')
        break