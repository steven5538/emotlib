# -*- coding: utf-8 -*-

import unittest
import random

import emotlib


class TestEmojiEmotlib(unittest.TestCase):
    def test_emoji(self):
        random.seed(0)
        test_answer = u'\U0001f3cc\U0001f3fe\u200d\u2640\ufe0f'
        self.assertEquals(emotlib.emoji(), test_answer)

        test_answer = u'\U0001f349'
        self.assertEquals(emotlib.emoji(category='food-fruit'), test_answer)