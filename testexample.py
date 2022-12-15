import unittest
# assert sum([1, 1, 2]) == 3, 'error'


def my_fuc(n1, n2):
    return n1 + n2 + 3


# assert my_fuc(1, 1) == 2, 'error'


class TestMyFunc(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual(my_fuc(1, 1), 2, 'should return 2')


unittest.main()
