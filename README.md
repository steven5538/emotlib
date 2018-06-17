# emotlib: Python emoji + emoticon Library


![PyPI - Python Version](https://img.shields.io/pypi/pyversions/emotlib.svg)
![PyPI](https://img.shields.io/pypi/v/emotlib.svg)
![Travis branch](https://img.shields.io/travis/steven5538/emotlib/master.svg)
![Coveralls github](https://img.shields.io/coveralls/github/steven5538/emotlib.svg)
![PyPI - License](https://img.shields.io/pypi/l/emotlib.svg)


Installation
------------

To install emotlib, simply use [pipenv](http://pipenv.org/) (or pip, of course):
```
$ pipenv install emotlib
🍩🎉
```
Satisfaction guaranteed.

Example
-------------

Note: In python2.x, your string need to be unicode. Ex: u'I\'m :elf:'
``` python
>> import emotlib
>> print(emotlib.emoji())
🧙‍
>> print(emotlib.emoji(category='food-fruit'))
🍉
>> print(emotlib.emoji(num=3))
👨‍🚀👨‍🚀👨‍🚀
>> print(emotlib.emoji(num=3, sep= ' ~ '))
🤸 ~ 🤸 ~ 🤸 ~ 
>> print(emotlib.emojify('I\'m :man_technologist:'))
I'm 👨‍💻
>> print(emotlib.emojify('I\'m :man~technologist:', alias='~'))
I'm 👨‍💻
>> print(emotlib.demojify('I\'m 👨‍💻'))
I'm :man_technologist:
>> print(emotlib.demojify('I\'m 👨‍💻', alias='~'))
I'm :man~technologist:


>> print(emotlib.emoticon())
( ´ ▽ ` )ﾉ
>> print(emotlib.emoticon(feel='confused'))
(´−｀) ﾝｰ
>> print(emotlib.emoticon(num=3))
┌（★ｏ☆）┘┌（★ｏ☆）┘┌（★ｏ☆）┘
>> print(emotlib.emoticon(num=3, sep=' ~ '))
(´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ 
>> print(emotlib.emoticonify('I\'m a happy developer.'))
I'm a happy developer. *(*´∀｀*)☆
```

Check categories & feels
```python
>> import emotlib
>> emotlib.emoji_categories
>> emotlib.emoticon_feels
```