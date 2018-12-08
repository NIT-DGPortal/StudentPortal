import unittest

import pro1


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(pro1.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
