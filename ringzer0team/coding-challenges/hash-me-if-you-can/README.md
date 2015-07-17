# [Hash Me If You Can](http://ringzer0team.com/challenges/13)

I used python to solve this challenge. I wrote [a python script](https://github.com/alirezaomidi/ctf/blob/master/ringzer0team/coding-challenges/hash-me-if-you-can/code.py). This script starts a session in [ringzer0team](http://ringzer0team.com) website. Then grabs the message from [the challenge page](http://ringzer0team.com/challenges/13), hashes it with [SHA512 Algorithm](https://en.wikipedia.org/wiki/SHA-2) and sends it back to [the challenge page](http://ringzer0team.com/challenges/13).

For more information, look at [the code](https://github.com/alirezaomidi/ctf/blob/master/ringzer0team/coding-challenges/hash-me-if-you-can/code.py).

Let's use it:

```
$ python code.py
Enter your ringzer0team username: [your_username]
Enter your ringzer0team password: [your_password]
FLAG-mukgu5g2w932t2kx1nqnhhlhy4
```

so the flag is **FLAG-mukgu5g2w932t2kx1nqnhhlhy4**

* You should install [requests](http://docs.python-requests.org/en/latest/user/install) python package. try: `pip install requests`. If you don't have `pip` package too, read [the docs](http://docs.python-requests.org/en/latest/user/install) to see how to install the needed packages.