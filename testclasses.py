# import lotoclasses as loto
from lotofunctions2 import Person, Computer, Game

def test_card():
    player = Person()

    card = player.create_card()
    assert len(card) == 3
    assert len(card[0]) == len(card[1]) == len(card[1]) == 9

def test_player_delete():
    player = Person()
    card = player.my_card
    n = player.my_card[0][6]
    actions = 'y'
    res = player.delete(n,actions)
    assert res == 0
    n = player.my_card[0][6]
    actions = 'n'
    res = player.delete(n,actions)
    assert res == 1
    n = 125
    actions = 'y'
    res = player.delete(n,actions)
    assert res == 1
    actions = 'n'
    res = player.delete(n, actions)
    assert res == 0

def test_computer_delete():
    player = Computer()
    card = player.my_card
    n = player.my_card[0][6]
    res = player.delete(n)
    assert (not any(n in sl for sl in player.my_card)) == True


def test_game_init():
    game = Game()
    assert game.players == []
    assert game.failed == []
    assert game.names == []
    assert len(game.bag) == 90



