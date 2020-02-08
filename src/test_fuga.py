import unittest
from .fuga import fuga


class TestFuga(unittest.TestCase):
    def test_fuga(self):
        self.assertEqual(-1, fuga(2, 3))

