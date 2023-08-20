from app.player_node import PlayerNode


class PlayerList:
    """A doubly-linked list containing `PlayerNodes`

    Attributes
    ----------
    head
        a reference to the first `PlayerNode` in the list
    tail
        a reference to the last `PlayerNode` in the list
    """

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
        """Returns `True` if the list is empty"""
        return self._head is None

    def insert_head(self, node: PlayerNode) -> None:
        """Inserts a `PlayerNode` at the head of the list

        Parameters
        ----------
        node
            the node to insert
        """
        if self.is_empty():
            self._head = node
            self._tail = node
            return

        node.next = self.head
        node.next.previous = node
        self._head = node

    def insert_tail(self, node: PlayerNode) -> None:
        """Inserts a `PlayerNode` at the tail of the list

        Parameters
        ----------
        node
            the node to insert
        """
        if self.is_empty():
            self.insert_head(node)
            return

        node.previous = self.tail
        node.previous.next = node
        self._tail = node

    def get(self, index: int) -> PlayerNode:
        """Gets the `PlayerNode` at a given index

        Parameters
        ----------
        index
            the index of the node to get

        Returns
        -------
        PlayerNode
            the node at the given index

        Raises
        ------
        IndexError
            if no node is at the given index
        """

        current_node = self.head
        for idx in range(index):
            try:
                current_node = current_node.next
            except AttributeError:
                break

        if current_node is None:
            raise IndexError("Index out of bounds")

        return current_node

    def display(self, forward: bool = True) -> None:
        """Prints the list of nodes in a human-readable format

        Parameters
        ----------
        forward
            if false, the nodes are printed in reverse
        """
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next

        if forward is False:
            nodes.reverse()

        [print(node) for node in nodes]

    def del_head(self):
        """Deletes the head node and sets the next
        node as the head (if it exists)

        Raises
        ------
        IndexError
            if the list is empty
        """
        if self.is_empty():
            raise IndexError("Index out of bounds")

        if self.head == self.tail:
            self._head = self._tail = None
            return

        self._head = self.head.next
        if self.head:
            self.head.previous = None

    def del_tail(self):
        """Deletes the tail node and sets the previous
        node as the tail (if it exists)

        Raises
        ------
        IndexError
            if the list is empty
        """
        if self.is_empty():
            raise IndexError("Index out of bounds")

        if self.head == self.tail:
            self._head = self._tail = None
            return

        self._tail = self.tail.previous
        if self.tail:
            self.tail.next = None

    def delete(self, index: int) -> None:
        """Deletes the node at a given index, adjusting
        the next and previous nodes to fill the gap

        Parameters
        ----------
        index
            the index of the node to delete

        Raises
        ------
        IndexError
            if no node is at the given index
        """
        node_to_del = self.get(index)
        if node_to_del == self.head:
            self._head = node_to_del.next

        if node_to_del == self.tail:
            self._tail = node_to_del.previous

        if node_to_del.previous:
            node_to_del.previous.next = node_to_del.next

        if node_to_del.next:
            node_to_del.next.previous = node_to_del.previous
