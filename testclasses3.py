from lotofunctions3 import Card, Person, Computer, Game

def test_card():
    getcard = Card()

    card = getcard.create_card()
    assert len(card) == 3
    assert len(card[0]) == len(card[1]) == len(card[1]) == 9

def test_getrandomnum():
    game = Game()
    n = game.get_random_num()
    assert 0 < n < 91
    assert len(game.bag) == 89
def test_player_delete():
    player = Person()
    card = player.card
    for i in player.card[0]:
        if type(i) == int:
            n = i
            break
        else:
            continue

    actions = 'y'
    res = player.delete(n, actions)
    assert all(n not in sl for sl in player.card) == True

    assert res == 0
    n = player.card[0][6]
    actions = 'n'
    res = player.delete(n, actions)
    assert res == 1
    n = 125
    actions = 'y'
    res = player.delete(n, actions)
    assert res == 1
    actions = 'n'
    res = player.delete(n, actions)
    assert res == 0


def test_computer_delete():
    player = Computer()
    # card = player.card
    for i in player.card[0]:
        if type(i) == int:
            n = i
            break
        else:
            continue
    player.delete(n)
    assert all(n not in sl for sl in player.card) == True


def test_game_init():
    game = Game()
    assert game.players == []
    assert game.failed == []
    assert game.names == []
    assert len(game.bag) == 90

def test_game_over():
    game = Game()
    lst = [['-', ' ', ' ', ' '], [' ', ' '], [' ']]
    failed = [1,2]
    numplayers = 3
    result = game.game_over(lst, failed, numplayers)
    assert result == 'Gameover_vinner'
    lst = [['-', '1', ' ', ' '], [' ', ' '], [' ']]
    failed = [1, 2]
    numplayers = 3
    result = game.game_over(lst, failed, numplayers)
    assert result == 'Continue'
    lst = [['-', '1', ' ', ' '], [' ', ' '], [' ']]
    failed = [1, 2]
    numplayers = 2
    result = game.game_over(lst, failed, numplayers)
    assert result == 'Gameover'

