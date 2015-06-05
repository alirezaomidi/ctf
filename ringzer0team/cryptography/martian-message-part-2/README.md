# [Martian Message - Part 2](http://ringzer0team.com/challenges/63)

The cryptography method in this problem is [Vigenere Cipher](http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

The only thing you have to do is to write cipher text and key under it (repeat the key till it becomes the size of cipher text):

```
KDERE2UNX1W1H96GYQNUSQT1KPGB
fselkladfklklaklfselkladfklk
```

Then move each letter of the cipher text backward in the alphabet according to order of the key letter under it, in the alphabet! For example:

```
K    D    E    R
f:5  s:18 e:4  l:11
```

Becomes:

```
FLAG
```

* When you encounter a non-alphabetical character, just write it in the plain text.
* To encipher a plain text do so except moving backward. You should move forward in the alphabet now.

So the flag is: **FLAGU2JNU1R1X96VOFNKHLB1GEWQ**

I wrote a [python script](vigenere.py) which helps you to decipher a cipher text ciphered by Vigenere Cipher.

Enjoy!