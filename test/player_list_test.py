import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class PlayerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ids = ('a123', 'b456')
        self.names = ('Alex', 'Casey')
        self.player_node_1 = PlayerNode(Player(self.ids[0], self.names[0]))
        self.player_node_2 = PlayerNode(Player(self.ids[1], self.names[1]))
        self.player_list = PlayerList()

    def test_insert_head_when_empty(self):
        self.assertIsNone(self.player_list.head,
                          "Head is not None")
        self.player_list.insert_head(self.player_node_1)
        self.assertEqual(self.player_list.head, self.player_node_1,
                         "Head is not player_node_1")
        self.assertIsNone(self.player_list.head.next,
                          "player_list.head.next is not None")

    def test_insert_head_when_not_empty(self):
        self.test_insert_head_when_empty()
        self.player_list.insert_head(self.player_node_2)
        self.assertEqual(self.player_list.head, self.player_node_2,
                         "player_list.head is not player_node_2")
        self.assertEqual(self.player_list.head.next, self.player_node_1,
                         "player_list.head.next is not player_node_1")
        self.assertEqual(self.player_list.head.next.previous, self.player_node_2,
                         "player_list.head.next.previous is not player_node_2")


if __name__ == '__main__':
    unittest.main()
