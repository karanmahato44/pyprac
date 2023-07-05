import unittest
import unittesting


class TestUnittesting(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(unittesting.sum(10, 20), 30)
        self.assertEqual(unittesting.sum(-1, 1), 0)
        self.assertEqual(unittesting.sum(-10, -20), -30)


if __name__ == '__main__':
    unittest.main()
