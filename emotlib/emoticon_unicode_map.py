# -*- coding: utf-8 -*-

# (<ゝω・)☆

__all__ = ['EMOTICON_UNICODE', 'EMOTICONS', 'EMOTICON_MOTIONS']

EMOTICON_UNICODE =  {
    u'happy': [
        u'( ͡° ͜ʖ ͡°)', u'∠( ᐛ 」∠)＿', u'(ﾟ⊿ﾟ)', u'ᕕ( ᐛ )ᕗ', u'_へ__(‾◡◝ )>',
        u'( ᐛ )و', u'( ´ ▽ ` )ﾉ', u'(*^▽^*)', u'(´∇ﾉ｀*)ノ', u'(ノ^∇^)',
    ],
    u'worried': [
        u'( ´△｀)', u'(　ﾟдﾟ)', u'(⊙…⊙ )', u'＼(°o°；）', u'~~旦_(･o･;)',
        u'ヽ(*´Д｀*)ﾉ', u':;(∩´﹏`∩);:', u'｡:ﾟ*+;(●´･д･`●);+*ﾟ:｡', u'( ；´Д｀)', u'(-’๏_๏’-)',
    ]
}

EMOTICON_MOTIONS = list(EMOTICON_UNICODE.keys())
EMOTICONS = []
for motion in EMOTICON_UNICODE.keys():
    EMOTICONS += EMOTICON_UNICODE[motion]