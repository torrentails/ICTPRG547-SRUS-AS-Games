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

        old_head = self.head
        self._head = node
        node.next = old_head
        old_head.previous = node
