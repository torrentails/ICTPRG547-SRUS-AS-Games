from typing import Optional

from app.player import Player


class PlayerNode:
    """Node to contain a `Player` for use in a `PlayerList`

    Attributes
    ----------
    player
        the wrapped `Player` object
    next
        reference to the next `PlayerNode`
    previous
        reference to the previous `PlayerNode`
    key
        returns the uid of the wrapped `Player`
    """
    
    _player: Player
    _previous: Optional["PlayerNode"]
    _next: Optional["PlayerNode"]

    def __init__(self, player: Player):
        """
        Parameters
        ----------
        player
            The `Player` to wrap
        """
        self._player = player
        self._previous = None
        self._next = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def next(self) -> Optional["PlayerNode"]:
        return self._next

    @next.setter
    def next(self, val: "PlayerNode") -> None:
        self._next = val

    @property
    def previous(self) -> Optional["PlayerNode"]:
        return self._previous

    @previous.setter
    def previous(self, val: "PlayerNode") -> None:
        self._previous = val

    @property
    def key(self) -> str:
        return self.player.uid

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({str(self.player)})"