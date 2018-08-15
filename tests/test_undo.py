# was not included in the GUI
from ConnectFour import ConnectFour
import pytest

def test_undo():
    my = ConnectFour.Game()
    assert len(my.moves) == 0
    assert not my.undo_move()
    my.move(2)
    assert 2 in my.moves
    assert my.round == 2
    assert my.turn == 'Y'
    my.undo_move()
    assert my.turn == 'X'
    assert my.round == 1