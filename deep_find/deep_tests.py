import unittest
from deep_tasks import *


class TestDeepTasks(unittest.TestCase):

    def setUp(self):
        self.diki = {
            'A': {
                'C': [2, 5],
                'D': {
                    'I': 'heyo!',
                    'J': 6,
                    'F': 'In [A][D]'
                },
                'E': False
            },
            'B': {
                'F': 'In [B]',
                'G': None,
                'H': True
            }
        }

    def test_deep_find_with_target_in_top_level(self):

        result = deep_find(self.diki, 'B')
        expected = {'F': 'In [B]', 'G': None, 'H': True}

        self.assertEqual(result, expected)

    def test_deep_find_with_target_inside_first_branch(self):

        result = deep_find(self.diki, 'E')
        expected = False

        self.assertEqual(result, expected)

    def test_deep_find_with_target_outside_first_branch(self):

        result = deep_find(self.diki, 'J')
        expected = 6

        self.assertEqual(result, expected)

    def test_deep_find_with_duplicate_key(self):

        result = deep_find(self.diki, 'F')
        expected = 'In [A][D]'

        self.assertEqual(result, expected)

    def test_broad_find_with_target_in_top_level(self):

        result = broad_find(self.diki, 'B')
        expected = {'F': 'In [B]', 'G': None, 'H': True}

        self.assertEqual(result, expected)

    def test_broad_find_finds_correct_duplicate_key(self):

        result = broad_find(self.diki, 'F')
        expected = 'In [B]'

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
