# -*- coding: utf-8 -*-

import unittest

import emotlib


class TestDemojifyEmotlib(unittest.TestCase):
    def test_demojify(self):
        test_case = u'I\'m :man_technologist:'
        test_answer = u'I\'m 👨‍💻'
        self.assertEquals(emotlib.emojify(test_case), test_answer)

        test_case = u'I\'m :man~technologist:'
        test_answer = u'I\'m 👨‍💻'
        self.assertEquals(emotlib.emojify(test_case, alias='~'), test_answer)