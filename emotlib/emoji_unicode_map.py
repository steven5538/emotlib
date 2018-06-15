# -*- coding: utf-8 -*-

# 👨‍🚀👩‍🚀

__all__ = ['EMOJI_UNICODE', 'EMOJIS', 'EMOJI_CATEGORIES']

EMOJI_UNICODE = {
    'people': {
        u':male_astronaut:': u'👨‍🚀',
        u':female_astronaut:': u'👩‍🚀',
        u':male_mage:': u'🧙‍♂️',
        u':female_mage:': u'🧙‍',
    }
}

EMOJI_CATEGORIES = list(EMOJI_UNICODE.keys())
EMOJIS = []
for category in EMOJI_UNICODE.keys():
    EMOJIS += list(EMOJI_UNICODE[category].values())