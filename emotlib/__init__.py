# -*- coding: utf-8 -*-

# ('・ω・')

"""
Emoji + Emoticon Library
~~~~~~~~~~~~~~~~~~~~~~~~

emotlib is a library for Emoji and Emoticon, written in Python.
usage:

    >>> import emotlib
    >>> print(emotlib.emoji())
    👨‍🚀
    >>> print(emotlib.emoji(num=3))
    🧙‍🧙‍🧙‍
    >>> print(emotlib.emoticon())
    ( ´△｀)
    >>> print(emotlib.emoticon(num=5, sep=' ~ '))
    (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ 

Full documentation at <http://github.com/steven5538/emotlib>.

:copyright: (c) 2018 by steven5538.
:license MIT License, see LICENSE for more details.
"""

from random import choice

from .emoji_unicode_map import *
from .emoticon_unicode_map import *


def _multiple(emo, num=1, sep=''):
    num = 1 if num <= 1 else num
    sep = '' if num <= 1 else sep
    duplicate_unit = '%s%s' % (emo, sep)
    return duplicate_unit * num


def decorateMultiple(f):
    def wrapper(*args, **kargs):
        result = f(*args, **kargs)
        num = kargs.get('num', 1)
        seperator = kargs.get('sep', '')
        return _multiple(result, num, seperator)
    return wrapper


@decorateMultiple
def emoji(category='', num=1, sep=''):
    if category and category.lower() in EMOJI_CATEGORIES:
        return choice(list(EMOJI_UNICODE[category.lower()].values()))
    return choice(EMOJIS)


@decorateMultiple
def emoticon(feel='', num=1, sep=''):
    if feel and feel.lower() in EMOTICON_MOTIONS:
        return choice(EMOTICON_UNICODE[feel.lower()])
    return choice(EMOTICONS)
