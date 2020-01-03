# -*- coding: utf-8 -*-

from app.common.clsmod import SomeClass
import unittest


class ModClsTestCase(unittest.TestCase):
    """ Some class unittest """

    def setUp(self):
        self.obj = SomeClass()

    def test_mod(self):
        res = self.obj.add(1, 2)
        assert res
        self.assertEqual(res, 3)
