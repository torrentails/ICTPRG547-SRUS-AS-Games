from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    _head: PlayerNode | None
    _tail: PlayerNode | None

    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail

    def is_empty(self) -> bool:
        return self._head is None

    def insert_head(self, node: PlayerNode) -> None:
        if self.is_empty():
            self._head = node
            self._tail = node
            return

        node.next = self.head
        node.next.previous = node
        self._head = node

    def insert_tail(self, node: PlayerNode) -> None:
        if self.is_empty():
            self.insert_head(node)
            return

        node.previous = self.tail
        node.previous.next = node
        self._tail = node

    def del_head(self):
        if self.is_empty():
            raise IndexError("Index out of bounds")

        self._head = self.head.next
        if self.head:
            self.head.previous = None

    def del_tail(self):
        if self.is_empty():
            raise IndexError("Index out of bounds")

        self._tail = self.tail.previous
        if self.tail:
            self.tail.next = None
