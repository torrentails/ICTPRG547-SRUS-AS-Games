import unittest

from app.player import Player


class PlayerTest(unittest.TestCase):
    def test_properties(self):
        id = 'n357'
        name = 'Casey'
        player = Player(id, name)

        self.assertEqual(player.uid, id)
        self.assertEqual(player.name, name)


if __name__ == '__main__':
    unittest.main()
