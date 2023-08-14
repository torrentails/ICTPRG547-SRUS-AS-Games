from .player import Player
from .player_node import PlayerNode
from .player_list import PlayerList


# generate a PlayerList for easy use in interactive mode
def test_list() -> PlayerList:
    pn1 = PlayerNode(Player('123', "alex"))
    pn2 = PlayerNode(Player('456', "case"))
    pn3 = PlayerNode(Player('789', "doug"))
    pl = PlayerList()
    pl.insert_head(pn1)
    pl.insert_tail(pn2)
    pl.insert_tail(pn3)
    return pl
