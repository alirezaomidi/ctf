# [Words Mean Something](http://ringzer0team.com/challenges/42)

This challenge is about [cookie!](https://en.wikipedia.org/wiki/HTTP_cookie) not the sweet one, The HTTP one!

Let's look at this page's cookies:
1. Press <kbd>F12</kbd> to see Developer Options in your browser.
2. Find *Resources* tab, then cookies.
3. Click on *ringzer0team.com* cookie.

You see **flag** value is **0**. Maybe it should be **1**!

To change it in the *Console* tab in Developer Options:
```
> document.cookie = "flag=1"
```
or if you want to save the session:
```
> document.cookie = document.cookie.replace("flag=0", "flag=1")
```

Press refresh the page and here is the flag: **FLAG-AnlAb6QxDpQvg1yn2bAhyOJw**

Enjoy!