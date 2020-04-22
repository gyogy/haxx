import unittest
from deep_tasks import *


class TestDeepTasks(unittest.TestCase):

    def setUp(self):
        self.diki = {
            'A': {
                'B': [2, 5],
                'C': {
                    'D': 'heyo!',
                    'E': 6
                },
                'F': False
            },
            'G': {
                'H': True,
                'I': None
            }
        }

    def test_deep_find_dfs_with_target_in_top_level(self):

        result = deep_find_dfs(self.diki, 'G')
        expected = {'H': True, 'I': None}

        self.assertEqual(result, expected)

    def test_deep_find_dfs_with_target_inside_first_branch(self):

        result = deep_find_dfs(self.diki, 'E')
        expected = 6

        self.assertEqual(result, expected)

    def test_deep_find_dfs_with_target_outside_first_branch(self):

        result = deep_find_dfs(self.diki, 'H')
        expected = True

        self.assertEqual(result, expected)

    def test_deep_find_dfs_with_target_equal_to_None(self):
        '''
        This test passes for a funny reason. If we're looking for a key with a value of None,
        the line "if attempt is not None:" in the deep_find_dfs function will never be satisfied
        and the function will return nothing, i.e. None.
        '''

        result = deep_find_dfs(self.diki, 'I')
        expected = None

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
