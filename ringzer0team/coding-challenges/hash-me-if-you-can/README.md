# [Hash Me If You Can](http://ringzer0team.com/challenges/13)

I used python to solve this challenge. I wrote [a python script](https://github.com/alirezaomidi/ctf/blob/master/ringzer0team/coding-challenges/hash-me-if-you-can/code.py). There is a method called **get_flag** in that script which gives you the flag. Let's use it:

```
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import code
>>> code.get_flag('your_username', 'your_password')
u'FLAG-mukgu5g2w932t2kx1nqnhhlhy4'
```

* Instead of *your_username* and *your_password* type your [ringzer0team](http://ringzer0team.com) username and password respectively.
* [code.py](https://github.com/alirezaomidi/ctf/blob/master/ringzer0team/coding-challenges/hash-me-if-you-can/code.py) should be in your current directory.
* You should install [requests](http://docs.python-requests.org/en/latest/user/install) python package. try: `pip install requests`. If you don't have `pip` package too, read [the docs](http://docs.python-requests.org/en/latest/user/install) to see how to install the needed packages.