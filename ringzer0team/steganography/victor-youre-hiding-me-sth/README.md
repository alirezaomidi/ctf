# Victor You Are Hiding Me Something

This is an old steganography trick. Just concatenate the first letters of each line:

First copy the poetry to a file. Here we call it **poetry.txt**. Then in a Linux command line do:
```
$ grep -Po '^.' poetry.txt | tr -d '\n'
FLAGCMPHDDSQNUCCPNNSOQACJOOP
```

Easy! Wasn't it?!