import unittest
from .hoge import hoge


class TestHoge(unittest.TestCase):
    def test_hoge(self):
        self.assertEqual(5, hoge(2, 3))

