# [Brainsick](http://ringzer0team.com/challenges/122)

When we encounter a challenge with no description, We should think of hidden files. Let's take a look at the hexdump:
```
$ xxd 5411333e505440020a1799da6071851b.gif | less
0000000: 4749 4638 3961 b801 8101 f700 0000 0000  GIF89a..........
0000010: 0000 3300 0066 0000 9900 00cc 0000 ff00  ..3..f..........
0000020: 2b00 002b 3300 2b66 002b 9900 2bcc 002b  +..+3.+f.+..+..+
:
```
After searching about the `flag`:
```
00131c0: c9b3 4175 1293 b4b9 d525 1025 959a db4c  ..Au.....%.%...L
00131d0: 347d c969 8ecf aeb7 8f80 0000 3b52 6172  4}.i........;Rar
00131e0: 211a 0700 cf90 7300 000d 0000 0000 0000  !.....s.........
00131f0: 005e 0974 2090 2d00 a932 0100 8434 0100  .^.t .-..2...4..
0013200: 021d 01c3 6b49 86fa 441d 3308 0020 0000  ....kI..D.3.. ..
0013210: 0066 6c61 672e 6769 6600 f085 9c97 0dd9  .flag.gif.......
0013220: 1401 089d 9998 1195 8f46 5d80 898a ccd7  .........F].....
0013230: 6026 44c3 7661 b13d 1898 d33a 0a60 b30d  `&D.va.=...:.`..
/flag
```
There is a `flag.gif` file! Oh, Look at the second line. At address `00131dd`. It is `Rar!....`, the magic number(signature) of **RAR Archive version 5.0**. Let's use `dd` command to copy from `00131dd` to the end of file in order to achieve the RAR file. `dd` takes decimal numbers as input so first convert `131dd` to decimal: `78301`. Then:
```
$ dd if=5411333e505440020a1799da6071851b.gif bs=1 skip=78301 of=flag.rar
78301 of=flag.rar
78577+0 records in
78577+0 records out
78577 bytes (79 kB) copied, 0.118177 s, 665 kB/s
```
If we look in the RAR file, we see the `flag.gif` as we saw its name in the hexdump. We open it and TADA!!:

![Flag](flag/flag.gif)

The flag is **FLAG-Th2K4s83uQh9xA**

Enjoy!
