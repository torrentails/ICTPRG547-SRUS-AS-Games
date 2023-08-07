from app.player_node import PlayerNode


class PlayerList:
    _head: PlayerNode | None  # Change to Node when implemented

    def __init__(self):
        self._head = None

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    def is_empty(self) -> bool:
        return self._head is None

    def insert_head(self, node: PlayerNode) -> None:
        if self.is_empty():
            self._head = node
            return

        old_head = self.head
        self._head = node
        node.next = old_head
        old_head.previous = node
