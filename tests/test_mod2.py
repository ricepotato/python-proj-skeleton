# -*- coding: utf-8 -*-

from app.mod2 import mod_func
import unittest


class BasicTestMod2(unittest.TestCase):
    """Basic test mpd."""

    def test_mod(self):
        res = mod_func()
        assert res


if __name__ == '__main__':
    unittest.main()
