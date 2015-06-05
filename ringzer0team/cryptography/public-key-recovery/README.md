# [Public Key Recovery](http://ringzer0team.com/challenges/50)

In this problem we need an RSA tool. Here we use **OpenSSL** command line tool.

Ubuntu/Debian: `sudo apt-get install openssl`

Copy and paste the RSA private key to a file. Here we call it `prikey.pem`. Now:

```
$ openssl rsa -in prikey.pem -out pubkey.pem -pubout
writing RSA key
$ cat pubkey.pem
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwkrxVrZ+KCl1cX27SHDI7Efgn
FJZ0qTHUD6uEeSoZsiVkcu0/XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3
Lqqwcuhgypd3Sf/bH3z4tC25eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIU
tmpouI1IXqxjrDx2SQIDAQAB
-----END PUBLIC KEY-----
```

We need to copy the Base64 blob (between -BEGIN- and -END- tags) and submit it. Let's do it geeky! :

```
$ cat pubkey.pem | tail -n 5 | head -n 4 | tr -d '\n' | xclip -sel clipboard
```

* Hint: Install `xclip` tool before: `sudo apt-get install xclip`

This will remove _new lines_ and copy it to the clipboard. Submit it to the Problem and get the _flag_: **FLAG-9869O2dQ43d1r116kfD0Sj5n**

Enjoy!