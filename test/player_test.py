import unittest

from app.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.player_uid = '357'
        self.player_name = 'Casey'
        self.password = 'HelloWorld-1'
        self.player = Player(self.player_uid, self.player_name)

    def test_properties(self):
        self.assertEqual(self.player.uid, self.player_uid,
                         f"player.uid is not {self.player_uid}")
        self.assertEqual(self.player.name, self.player_name,
                         f"player.name is not {self.player_name}")

    def test_add_password(self):
        self.player.add_password(self.password)
        self.assertRaises(RuntimeError, self.player.add_password, "SomeOtherPass456")
        self.assertRaises(RuntimeError, self.player.add_password, self.password)

        self.assertTrue(self.player.verify_password(self.password))

    def test_verify_password(self):
        self.assertRaises(RuntimeError, self.player.verify_password, self.password)
        self.assertRaises(RuntimeError, self.player.verify_password, "SomePass!9")

        self.player.add_password(self.password)
        self.assertTrue(self.player.verify_password(self.password))
        self.assertFalse(self.player.verify_password("a_failing_pass"))


if __name__ == '__main__':
    unittest.main()
