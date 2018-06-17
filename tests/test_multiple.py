# -*- coding: utf-8 -*-

import unittest
import emotlib


class TestMultipleEmotlib(unittest.TestCase):
    def setUp(self):
        self.test_emoji = u'🧙‍♂️'

    def test_multiple(self):
        test_case = self.test_emoji
        self.assertEquals(test_case, emotlib._multiple(self.test_emoji))

        test_case = self.test_emoji
        self.assertEquals(test_case, emotlib._multiple(self.test_emoji, num=-1))

        test_case = self.test_emoji
        self.assertEquals(test_case, emotlib._multiple(self.test_emoji, sep='!!%!%'))

        test_case = self.test_emoji
        self.assertEquals(test_case, emotlib._multiple(self.test_emoji, num=-3, sep='!!%!%'))

        test_case = self.test_emoji * 3
        self.assertEquals(test_case, emotlib._multiple(self.test_emoji, num=3))

        test_case = ('%s%s' % (self.test_emoji, ' !! ')) * 3
        self.assertEquals(test_case, emotlib._multiple(self.test_emoji, num=3, sep=' !! '))
