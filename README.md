# emotlib: Python emoji + emoticon Library

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

``` python
>> import emotlib
>> print(emotlib.emoji())
🧙‍
>> print(emotlib.emoji(num=3))
👨‍🚀👨‍🚀👨‍🚀
>> print(emotlib.emoticon())
( ´ ▽ ` )ﾉ
>> print(emotlib.emoticon(num=5, sep=' ~ '))
(´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ (´∇ﾉ｀*)ノ ~ 
```
