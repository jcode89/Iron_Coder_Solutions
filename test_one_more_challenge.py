import unittest

from one_more_challenge import add_one

class TestOneMoreChallenge(unittest.TestCase):
    def test_level_one(self):
        self.assertEqual([2, 1, 0, 6, 101, 38, 21, 19, 13, 1],
                        add_one([1, 0, -1, 5, 100, 37, 20, 18, 12, 0]))
    def test_level_two(self):
        self.assertEqual([2, 1, 0, 6, 101, 38, 21, 19, 13, 1],
                        add_one(['1', 'c', '0', '-1', '5', 'b', '100', '37', 'a', '20', '18', '12', '0']))
    def test_level_three(self):
        self.assertEqual(['ab124', 'gh01', 'ijk9', 'lmn13', 'cd100ef12'],
                        add_one(['ab123', 'gh00', 'ijk8', 'lmn12', 'cd99ef11']))
    def test_example_one(self):
        self.assertEqual([2, 3, 4], add_one([1, 2, 3]))
    def test_example_two(self):
        self.assertEqual([2, 4], add_one(['1', 'b', '3']))
    def test_example_three(self):
        self.assertEqual(['ab13', 'a6', 'b24a52'],
                        add_one(['ab12', 'a5', 'b23a51']))

if __name__ == '__main__':
    unittest.main()
