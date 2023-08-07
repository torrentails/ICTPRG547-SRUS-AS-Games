import unittest

from app.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.player_id = 'n357'
        self.player_name = 'Casey'
        self.player = Player(self.player_id, self.player_name)

    def test_properties(self):

        self.assertEqual(self.player.uid, self.player_id,
                         f"player.uid is not {self.player_id}")
        self.assertEqual(self.player.name, self.player_name,
                         f"player.name is not {self.player_name}")


if __name__ == '__main__':
    unittest.main()
