import unittest

from website.txt2tei.errors import consolidate_positions

class TestErrorMarkup(unittest.TestCase):

    def consolidate_positions_Test(self):
        positions = [
            [0, 35],
            [17, 40],
            [44, 50],
            [55, 57],
            [56, 60]
        ]
        result = [
            [0, 40],
            [44, 50],
            [55, 60]
        ]

        self.assertEqual(consolidate_positions(positions), result)


if __name__ == 'main':
    unittest.main()