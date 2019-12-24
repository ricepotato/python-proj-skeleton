# -*- coding: utf-8 -*-

from app.common.mod import mod_func
import unittest


class BasicTestMod(unittest.TestCase):
    """Basic test mpd."""

    def test_mod(self):
        res = mod_func()
        assert res
