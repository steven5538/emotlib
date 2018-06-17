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
import re

from .emoji_unicode_map import *
from .emoticon_unicode_map import *


_EMOJI_REGEX_CACHE = None
emoji_categories = EMOJI_CATEGORIES
emoticon_feels = EMOTICON_FEELS


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
def emoticon(feel='', num=1, sep=''):
    if feel and feel.lower() in EMOTICON_FEELS:
        return choice(EMOTICON_UNICODE[feel.lower()])
    return choice(EMOTICONS)


def emoticonify(text):
    """Add feeling emoticon to the end of text.

        >>> import emotlib
        >>> emotlib.emoticonify('I\'m a happy developer.')
        I'm a happy developer. (ᅌᴗᅌ* )
    """

    return text + ' ' + ''.join([choice(EMOTICON_UNICODE.get(t, [''])) for t in text.split()])


@decorateMultiple
def emoji(category='', num=1, sep=''):
    if category and category.lower() in EMOJI_CATEGORIES:
        return choice(list(EMOJI_UNICODE[category.lower()].values()))
    return choice(EMOJIS)


def emojify(text, alias='_'):
    """Replace CLDR to emoji. Use to show.
    Default alias "_".

        >>> import emotlib
        >>> emotlib.emojify('I\'m :man_technologist:')
        I'm 👨‍💻
        >>> emotlib.emojify('I\'m :man~technologist:', alias='~')
        I'm 👨‍💻
    """

    pattern = re.compile(u'(:[%sa-zA-Z0-9&.()!$_ ]*:)' % alias)

    def repl(match):
        val = match.group(1)[1:-1].replace(alias, ' ')
        return EMOJI_UNICODE_WITHOUT_CATEGORY.get(val, val)

    return pattern.sub(repl, text)


def demojify(text, alias='_'):
    """Replace emoji to CLDR. Useful if you need to store.
    Default alias "_".

        >>> import emotlib
        >>> emotlib.demojify('I\'m 👨‍💻')
        I'm :man_technologist:
        >>> emotlib.demojify('I\'m 👨‍💻', alias='~')
        I'm :man~technologist:
    """

    def repl(match):
        val = UNICODE_EMOJI_WITHOUT_CATEGORY.get(match.group(0), match.group(0))
        return ':' + alias.join(val[:].split()) + ':'

    return _emoji_regex_cache().sub(repl, text)


def _emoji_regex_cache():
    global _EMOJI_REGEX_CACHE

    if _EMOJI_REGEX_CACHE is None:
        emojis = sorted(EMOJIS, key=len, reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEX_CACHE = re.compile(pattern)

    return _EMOJI_REGEX_CACHE
