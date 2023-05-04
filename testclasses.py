import lotoclasses as loto

def test_card():
    player = loto.Person()

    card = player.create_card()
    assert len(card) == 3
    assert len(card[0]) == len(card[1]) == len(card[1]) == 9

def test_player_delete():
    player = loto.Person()
    card = player.my_card
    n = player.my_card[0][6]
    actions = 'y'
    res = player.delete(n,card,actions)
    assert res == 0
    n = player.my_card[0][6]
    actions = 'n'
    res = player.delete(n,card,actions)
    assert res == 1
    n = 125
    actions = 'y'
    res = player.delete(n, card, actions)
    assert res == 1
    actions = 'n'
    res = player.delete(n, card, actions)
    assert res == 0

def test_computer_delete():
    player = loto.Computer()
    card = player.my_card
    n = player.my_card[0][6]
    res = player.delete(n, card)
    assert res == 0
    n = 125
    res = player.delete(n, card)
    assert res == 1



