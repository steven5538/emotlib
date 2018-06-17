# -*- coding: utf-8 -*-

import unittest
import random

import emotlib


class TestEmoticonifyEmotlib(unittest.TestCase):
    def test_emoticonify(self):
        random.seed(0)
        test_case = u'I\'m a happy developer.'
        test_answer = u'I\'m a happy developer. ( ﾉ^.^)ﾉﾟ'
        self.assertEquals(emotlib.emoticonify(test_case), test_answer)