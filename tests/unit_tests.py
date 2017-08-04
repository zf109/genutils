#!/c/Users/zfeng/AppData/Local/Continuum/Anaconda3/python

from unittest import TestCase
import unittest
from .context import listoperation

class TestListOperation(TestCase):

    def setUp(self):
        self.test_list = [[1,3], [2,4], [5,6], [1,2]]

    def test_flat_list(self):
        self.assertEqual([1, 3, 2, 4, 5, 6, 1, 2], flat_list(self.test_list))

if __name__ == "__main__":
    unittest.main()
