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

    def test_df_dfs_with_target_in_top_level(self):

        result = df_dfs(self.diki, 'B')
        expected = {'F': 'In [B]', 'G': None, 'H': True}

        self.assertEqual(result, expected)

    def test_df_dfs_with_target_inside_first_branch(self):

        result = df_dfs(self.diki, 'E')
        expected = False

        self.assertEqual(result, expected)

    def test_df_dfs_with_target_outside_first_branch(self):

        result = df_dfs(self.diki, 'J')
        expected = 6

        self.assertEqual(result, expected)

    def test_df_dfs_with_duplicate_key(self):

        result = df_dfs(self.diki, 'F')
        expected = 'In [A][D]'

        self.assertEqual(result, expected)

    def test_df_bfs_with_target_in_top_level(self):

        result = df_bfs(self.diki, 'B')
        expected = {'F': 'In [B]', 'G': None, 'H': True}

        self.assertEqual(result, expected)

    def test_df_bfs_finds_correct_duplicate_key(self):

        result = df_bfs(self.diki, 'F')
        expected = 'In [B]'

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
