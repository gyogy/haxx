import unittest
from deep_tasks import *


class TestFindFuncs(unittest.TestCase):

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


class TestFindAllFuncs(unittest.TestCase):

    def setUp(self):
        self.dic = {
            'A': {
                'C': [2, 5],
                'D': {
                    'I': 'heyo!',
                    'C': 6,
                    'F': 'In [A][D]'
                },
                'E': False
            },
            'B': {
                'F': 'In [B]',
                'C': None,
                'H': True
            }
        }

    def test_if_deep_f_all_is_depth_first(self):

        result = list()
        expected = ['In [A][D]', 'In [B]']

        for hit in deep_f_all(self.dic, 'F'):
            result.append(hit)

        self.assertEqual(result, expected)

    def test_deep_f_all_with_key_not_in_data(self):

        result = list()
        expected = []

        for hit in deep_f_all(self.dic, 'Z'):
            result.append(hit)

        self.assertEqual(result, expected)

    def test_if_broad_f_all_is_breadth_first(self):
        result = list()
        expected = [[2, 5], None, 6]

        for hit in broad_f_all(self.dic, 'C'):
            result.append(hit)

        self.assertEqual(result, expected)


class TestDeepUpdate(unittest.TestCase):

    def setUp(self):
        self.dic = {
            'A': {
                'C': '[2, 5]',
                'D': {
                    'I': 'heyo!',
                    'C': '6',
                    'F': 'In [A][D]'
                },
                'E': 'False'
            },
            'B': {
                'F': 'In [B]',
                'C': 'None',
                'H': 'True'
            }
        }

    def test_deep_update_changing_nested_dict_to_string(self):

        result = deep_update(self.dic, 'D', True)
        expected = {
            'A': {
                'C': '[2, 5]',
                'D': True,
                'E': 'False'
            },
            'B': {
                'F': 'In [B]',
                'C': 'None',
                'H': 'True'
            }
        }

        self.assertEqual(result, expected)

    def test_deep_update_changes_values_for_all_matching_keys(self):

        result = deep_update(self.dic, 'C', True)
        expected = {
            'A': {
                'C': True,
                'D': {
                    'I': 'heyo!',
                    'C': True,
                    'F': 'In [A][D]'
                },
                'E': 'False'
            },
            'B': {
                'F': 'In [B]',
                'C': True,
                'H': 'True'
            }
        }

        self.assertEqual(result, expected)


class TestDeepApply(unittest.TestCase):

    def setUp(self):
        self.dic = {
            'A': {
                'list': [2, 5],
                'C': {
                    'str': 'a',
                    'int': 6,
                },
                'bool': False
            },
            'B': None,
        }

    def test_deep_apply_with_simple_times_two_function(self):

        result = deep_apply(times_two, self.dic)
        expected = {
            'A': {
                'list': [2, 5, 2, 5],
                'C': {
                    'str': 'aa',
                    'int': 12,
                },
                'bool': 0
            },
            'B': None,
        }

        self.assertEqual(result, expected)


class TestSchemaValidator(unittest.TestCase):

    def setUp(self):
        self.schema = [
            'key1',
            'key2', [
                'key3', [
                    'inner_key1',
                    'inner_key2'
                ]
            ]
        ]

        self.valid_dic = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        }

        self.inval_dic = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            },
            'key4': 'not expected'
        }

    def test_schema_validator_validates_valid_dic(self):

        result = schema_validator(self.schema, self.valid_dic)
        expected = True

        self.assertEqual(result, expected)

    def test_schema_validator_doesnt_validate_inval_dic(self):

        result = schema_validator(self.schema, self.inval_dic)
        expected = False

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
