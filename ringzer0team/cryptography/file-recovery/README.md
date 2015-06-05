# [File Recovery](http://ringzer0team.com/challenges/49)

After downloading the archive, extract it. There is a *flag* directory which contains these 2 files:

1. `private.pem` which is a *private RSA key*.
2. `flag.end` which is an *encoded RSA file*.

we use `rsautl` from `openssl` in command line:

```
$ openssl rsautl -decrypt -inkey private.pem -in flag.enc
FLAG-vOAM5ZcReMNzJqOfxLauakHx
```

Enjoy!