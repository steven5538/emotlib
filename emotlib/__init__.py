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
    >>> print(emotlib.emoticon())
    ( ´△｀)

Full documentation at <http://github.com/steven5538/emotlib>.

:copyright: (c) 2018 by steven5538.
:license MIT License, see LICENSE for more details.
"""

from random import choice

from .emoji_unicode_map import *
from .emoticon_unicode_map import *

def emoji(category=''):
    if category and category.lower() in EMOJI_CATEGORIES:
        return choice(list(EMOJI_UNICODE[category.lower()].values()))
    return choice(EMOJIS)

def emoticon(feel=''):
    if feel and feel.lower() in EMOTICON_MOTIONS:
        return choice(EMOTICON_UNICODE[feel.lower()])
    return choice(EMOTICONS)
