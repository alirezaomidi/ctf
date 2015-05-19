# Look Inside The House

There is something hidden in the image. To gain that, we use [Steghide](http://steghide.sourceforge.net/download.php) command line tool.

Ubuntu / Debian: `sudo apt-get install steghide`

First Let's see if there is a stegofile inside the image or not:
```
$ cd DIR
$ steghide info 3e634b3b5d0658c903fc8d42b033fa57.jpg
"3e634b3b5d0658c903fc8d42b033fa57.jpg":
  format: jpeg
  capacity: 7.0 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "flag.txt":
    size: 29.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

* **DIR** is where the image is.
* The **passphrase** is empty for this image. Just Press **Enter** key.

So there is a **flag.txt** in the image.

```
$ steghide extract -sf 3e634b3b5d0658c903fc8d42b033fa57.jpg
Enter passphrase:
the file flag.txt does already exist. overwrite ? (y/n) y
wrote extracted data to flag.txt.
```

The **flag.txt** file contains the **FLAG**:
```
$ cat flag.txt
FLAG-5jk682aqoepoi582r940oow
```

Enjoy!