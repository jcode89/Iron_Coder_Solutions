import unittest

from one_more_challenge import int_to_int, str_to_int, str_to_str

class TestOneMoreChallenge(unittest.TestCase):

    def test_level_one(self):
        self.assertEqual([2, 1, 0, 6, 101, 38, 21, 19, 13, 1],
                        int_to_int([1, 0, -1, 5, 100, 37, 20, 18, 12, 0]))

    def test_level_two(self):
        self.assertEqual([2, 1, 0, 6, 101, 38, 21, 19, 13, 1],
                        str_to_int(['1', 'c', '0', '-1', '5', 'b', '100', '37', 'a', '20', '18', '12', '0']))

    def test_level_three(self):
        self.assertEqual(['ab124', 'gh01', 'ijk9', 'lmn13', 'cd100ef12'],
                        str_to_str(['ab123', 'gh00', 'ijk8', 'lmn12', 'cd99ef11']))

    def test_level_one_again(self):
        self.assertEqual([2, 3, 4], int_to_int([1, 2, 3]))

    def test_level_two_again(self):
        self.assertEqual([2, 4], str_to_int(['1', 'b', '3']))

    def test_level_three_again(self):
        self.assertEqual(['ab13', 'a6', 'b24a52'],
                        str_to_str(['ab12', 'a5', 'b23a51']))

    def test_absurd_level_three(self):
        self.assertEqual(['ab124', 'ab13', 'gh01', 'ijk9', 'a6','lmn13', 'b24a52', 'cd100ef12'],
            str_to_str(['ab123', 'ab12','gh00', 'ijk8', 'a5','lmn12', 'b23a51','cd99ef11']))

    def test_level_two_last_time(self):
        self.assertEqual([2323, -787, 5, 67, 99],
                        str_to_int(['harry', '2322', '-788', 'rob', '4', '66', '98', 'slappy']))

    def test_level_three_last_time(self):
        self.assertEqual(['a02', 'c09', 'fgf200hjh13', 'abd202', 'b6', 'zx124', 'xyz13', 'b24a52', 'cd100ef12'],
                        str_to_str(['a01', 'c08', 'fgf199hjh12', 'abd201', 'b5', 'zx123', 'xyz12', 'b23a51','cd99ef11']))

if __name__ == '__main__':
    unittest.main()
