# -*- coding: utf-8 -*-

import unittest

import emotlib


class TestDemojifyEmotlib(unittest.TestCase):
    def test_demojify(self):
        test_case = u'I\'m 👨‍💻'
        test_answer = u'I\'m :man_technologist:'
        self.assertEquals(emotlib.demojify(test_case), test_answer)

        test_case = u'I\'m 👨‍💻'
        test_answer = u'I\'m :man~technologist:'
        self.assertEquals(emotlib.demojify(test_case, alias='~'), test_answer)