import unittest

from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class PlayerListTest(unittest.TestCase):
    def setUp(self) -> None:
        player_ids = ('a123', 'b456')
        player_names = ('Alex', 'Casey')
        self.player_node_1 = PlayerNode(Player(player_ids[0], player_names[0]))
        self.player_node_2 = PlayerNode(Player(player_ids[1], player_names[1]))
        self.player_list = PlayerList()

    def test_insert_head_when_empty(self):
        self.assertIsNone(self.player_list.head,
                          "player_list.head is not None")
        self.assertIsNone(self.player_list.tail,
                          "tail is not None")

        self.player_list.insert_head(self.player_node_1)

        self.assertEqual(self.player_list.head, self.player_node_1,
                         "player_list.head is not player_node_1")
        self.assertEqual(self.player_list.tail, self.player_node_1,
                         "player_list.tail is not player_node_1")
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

        self.assertEqual(self.player_list.tail, self.player_node_1,
                         "player_list.tail is not player_node_2")
        self.assertIsNone(self.player_list.tail.next,
                          "player_list.tail.next is not player_node_1")
        self.assertEqual(self.player_list.tail.previous, self.player_node_2,
                         "player_list.tail.previous is not player_node_2")


if __name__ == '__main__':
    unittest.main()
