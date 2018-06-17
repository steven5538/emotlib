# -*- coding: utf-8 -*-

import unittest
import random

import emotlib


class TestEmoticonEmotlib(unittest.TestCase):
    def test_emoticon(self):
        random.seed(0)
        test_answer = u'( •॒◞ ͜◟•॒ )'
        self.assertEquals(emotlib.emoticon(), test_answer)

        test_answer = u'∑（*☼＿☉*）'
        self.assertEquals(emotlib.emoticon(feel='crazy'), test_answer)