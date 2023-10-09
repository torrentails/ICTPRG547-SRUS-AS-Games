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

    def pop(self, index: int = None) -> PlayerNode:
        """Removes and returns the node at a given index, adjusting
        the next and previous nodes to fill the gap

        Parameters
        ----------
        index
            the index of the node to pop.
            If None, then the tail node is popped

        Returns
        -------
        PlayerNode
            the node removed from the indicated position of the list

        Raises
        ------
        IndexError
            if no node is at the given index
        """
        if self.is_empty():
            raise IndexError("Index out of bounds")

        if index is None:
            node_to_pop = self.tail

        else:
            node_to_pop = self.head
            for idx in range(index):
                try:
                    node_to_pop = node_to_pop.next
                except AttributeError:
                    break

        if node_to_pop is None:
            raise IndexError("Index out of bounds")

        if node_to_pop == self.head:
            self._head = node_to_pop.next

        if node_to_pop == self.tail:
            self._tail = node_to_pop.previous

        if node_to_pop.previous:
            node_to_pop.previous.next = node_to_pop.next

        if node_to_pop.next:
            node_to_pop.next.previous = node_to_pop.previous

        return node_to_pop

    def pop_left(self) -> PlayerNode:
        """Removes and returns the head node and sets the next
        node as the head (if it exists)

        Raises
        ------
        IndexError
            if the list is empty

        Returns
        -------
        PlayerNode
            the node removed from the beginning of the list
        """
        if self.is_empty():
            raise IndexError("Index out of bounds")

        return self.pop(0)
