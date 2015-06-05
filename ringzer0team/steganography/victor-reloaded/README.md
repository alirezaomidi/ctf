# [Victor Reloaded](http://ringzer0team.com/challenges/71)

This is a poetry from [Victor Hugo]() but with some issues. Some of the characters are wrong. Thanks to **Google** we can see the original poetry.

We have both of them in `issues.txt` and `original.txt`.

Do the following on a command line:
```
$ # split all of the characters for both files
$ # Then we can use diff on them
$ cat issues.txt | fold -w1 > ours.txt
$ cat original.txt | fold -w1 > victors.txt
$ diff -y --suppress-common-lines ours.txt victors.txt | cut -f9 | tr -d '\n'
flagarenice
```

So the flag is: **flagarenice**

* See both `ours.txt` and `victor.txt` and also the `diff` command's job here for more info!

**Enjoy!**