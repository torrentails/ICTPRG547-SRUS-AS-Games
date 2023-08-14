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

    def get(self, index: int) -> PlayerNode:
        current_node = self.head
        for idx in range(index):
            try:
                current_node = current_node.next
            except AttributeError:
                break

        if current_node is None:
            raise IndexError("Index out of bounds")

        return current_node

    def del_head(self):
        if self.is_empty():
            raise IndexError("Index out of bounds")

        if self.head == self.tail:
            self._head = self._tail = None
            return

        self._head = self.head.next
        if self.head:
            self.head.previous = None

    def del_tail(self):
        if self.is_empty():
            raise IndexError("Index out of bounds")

        if self.head == self.tail:
            self._head = self._tail = None
            return

        self._tail = self.tail.previous
        if self.tail:
            self.tail.next = None

    def delete(self, index: int) -> None:
        node_to_del = self.get(index)
        if node_to_del == self.head:
            self._head = node_to_del.next

        if node_to_del == self.tail:
            self._tail = node_to_del.previous

        if node_to_del.previous:
            node_to_del.previous.next = node_to_del.next

        if node_to_del.next:
            node_to_del.next.previous = node_to_del.previous
