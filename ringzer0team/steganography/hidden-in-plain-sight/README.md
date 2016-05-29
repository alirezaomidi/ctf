# [Hidden In Plain Sight](https://ringzer0team.com/challenges/188)

The text is an article named [Hacker Manifesto](http://www.phrack.org/issues/7/3.html#article) by [The Mentor](https://en.wikipedia.org/wiki/Loyd_Blankenship). It's a real inspiration written in 1980s.

We should take the hex dump of both texts (the original article and the challenge's article) and compare them. Keep the original article in `original.txt` and the challenge's article in `618d0e51213fa164d93bd92ca5e099c3.txt`.  
First extract the hex dump from the challenge's article:

```bash
xxd -p original.txt | fold -w 2 > org.hex
```

And for the challenge's article:
```bash
cat 618d0e51213fa164d93bd92ca5e099c3.txt | cut -d ' ' -f -16 | tr -d ' ' | fold -w 2 > chal.hex
```

Now compare the `.hex` files:
```bash
diff -y --suppress-common-lines *.hex > diff.txt
```

The output is:

```
46							      |	20
4c							      |	69
41							      |	65
47							      |	69
2d							      |	20
4e							      |	2c
6f							      |	20
74							      |	20
68							      |	20
69							      |	20
6e							      |	20
67							      |	6b
49							      |	74
73							      |	68
45							      |	73
76							      |	62
65							      |	6f
72							      |	68
57							      |	79
68							      |	65
61							      |	68
74							      |	6e
49							      |	77
74							      |	65
53							      |	20
65							      |	72
65							      |	20
6d							      |	65
73							      |	0a
```

Take the first column and convert to ASCII:

```bash
cat diff.txt | cut -f 1 | tr '\n' ' ' > flag.txt
```

Use Python:
```python
for i in open('flag.txt').readline().split():
  print(chr(int(i, 16)), end='')
```

The **FLAG** is: `FLAG-NothingIsEverWhatItSeems`
