from ConnectFour import ConnectFour
import pytest


def test_empty_cell():
    my = ConnectFour.Game()
    assert not my.check_for_win(2, 2)

def test_diagonal_win():
    # positive slope
    my = ConnectFour.Game()
    my.move(1)  # X
    my.move(2)  # Y
    my.move(2)  # YX
    my.move(3)  # Y
    my.move(3)  # YX
    my.move(4)  # Y
    my.move(3)  # YXX
    my.move(4)  # YY
    my.move(4)  # YYX
    my.move(6)  # Y
    my.move(4)  # YYXX
    assert my.check_for_win(3, 4)
    assert my.winner == 'X'
    winning_discs = [(3, 4), (2, 3), (1, 2), (0, 1)]
    returned_winning_discs = my.get_winning_discs()
    for disc in returned_winning_discs:
        assert disc in winning_discs
    for disc in winning_discs:
        assert disc in returned_winning_discs
    # game was already decided
    assert my.move(4) == None

    # negative slope
    my = ConnectFour.Game()
    my.move(6)  # X
    my.move(5)  # Y
    my.move(5)  # YX
    my.move(0)  # Y
    my.move(4)  # X
    my.move(4)  # XY
    my.move(4)  # XYX
    my.move(3)  # Y
    my.move(3)  # YX
    my.move(3)  # YXY
    my.move(3)  # YXYX
    assert my.check_for_win(3, 3)
    assert my.winner == 'X'
    returned_winning_discs = my.get_winning_discs()
    winning_discs = [(3, 3), (2, 4), (1, 5), (0, 6)]
    for disc in returned_winning_discs:
        assert disc in winning_discs
    for disc in winning_discs:
        assert disc in returned_winning_discs

def test_horizontal_win():
    my = ConnectFour.Game()
    # fill the first row
    for i in range(7):
        my.move(i)

    my.move(2)
    my.move(2)
    my.move(3)
    my.move(3)
    my.move(4)
    my.move(4)
    my.move(5)
    assert my.check_for_win(1, 5)
    assert my.winner == 'Y'
    winning_discs = [(1, 2), (1, 3), (1, 4), (1, 5)]
    returned_winning_discs = my.get_winning_discs()
    for disc in returned_winning_discs:
        assert disc in winning_discs
    for disc in winning_discs:
        assert disc in returned_winning_discs
    # game was already decided
    assert my.move(4) == None

def test_vertical_win():
    my = ConnectFour.Game()

    my.move(2)
    my.move(2)
    my.move(2)
    my.move(5)
    my.move(2)
    my.move(5)
    my.move(2)
    my.move(5)
    my.move(2)
    assert my.check_for_win(5, 2)
    assert my.winner == 'X'
    winning_discs = [(2, 2), (3, 2), (4, 2), (5, 2)]
    returned_winning_discs = my.get_winning_discs()
    for disc in returned_winning_discs:
        assert disc in winning_discs
    for disc in winning_discs:
        assert disc in returned_winning_discs
    # game was already decided
    assert my.move(4) == None

def test_draw():
    my = ConnectFour.Game()
    for col in range(3):
        for _ in range(6):
            my.move(col)
    my.move(6)
    for col in range(3, 7):
        for _ in range(6):
            my.move(col)
    # now the board is full, but no winners
    assert my.winner == 'D'
    my.print_board()

test_draw()