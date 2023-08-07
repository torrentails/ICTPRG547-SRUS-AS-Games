from typing import Optional

from app.player import Player


class PlayerNode:
    _player: Player
    _previous: Optional["PlayerNode"]
    _next: Optional["PlayerNode"]

    def __init__(self, player: Player):
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