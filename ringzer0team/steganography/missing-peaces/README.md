# [Missing Peaces](http://ringzer0team.com/challenges/129)

In the down-right corner of the image, there is a QRCode. Just scan it!

Here I cut the QR Code from the original image and called it **qr.png**. Then used `convert` tool from the [ImageMagick](http://www.imagemagick.org/script/binary-releases.php) package to make a black on white - readable QR Code:

```
$ convert qr.png -white-threshold 0 qr-bw.png
```

![QR Code](qr-bw.png)

Now scan it and here is the flag: **flag-517qBd4tesUTUomYdz7W**