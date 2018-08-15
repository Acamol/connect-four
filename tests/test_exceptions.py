from ConnectFour import ConnectFour
import pytest


def test_valid_move():
    my = ConnectFour.Game()

    with pytest.raises(ConnectFour.MoveOutOfRange):
        my.move(-1)
    assert my.round == 1
    assert my.turn == 'X'

    with pytest.raises(ConnectFour.MoveOutOfRange):
        my.move(7)
    assert my.round == 1
    assert my.turn == 'X'

    # fill column 2
    for _ in range(6):
        my.move(2)

    with pytest.raises(ConnectFour.FullColumn):
        my.move(2)
