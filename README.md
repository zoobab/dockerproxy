DockerProxy
===========

DockerProxy, a simple proxy for docker pull

Why?
====

Because you just want to download a tarball, not layers.

How to run the proxy?
=====================

It is a simple flask application, so you first need to install flask. 

You also need to run it on a host machine which has a docker daemon running.

Then launch it:

```
$ export FLASK_APP=dockerproxy.py
$ flask run 
 * Serving Flask app "dockerproxy"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Wget client
===========

After that you can try with the busybox image for example:

```
$ wget http://127.0.0.1:5000/dl?myimage=busybox
--2018-06-17 12:29:21--  http://127.0.0.1:5000/dl?myimage=busybox
Connecting to 127.0.0.1:5000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 47714304 (46M) [application/octet-stream]
Saving to: ‘dl?myimage=busybox’

dl?myimage=busybox         100%[=====================================>]  45.50M  --.-KB/s    in 0.1s    

2018-06-17 12:29:27 (365 MB/s) - ‘dl?myimage=busybox’ saved [47714304/47714304]

```

In the logs of the server, you should see:

```
Downloading image: busybox....
Using default tag: latest
latest: Pulling from library/busybox
Digest: sha256:141c253bc4c3fd0a201d32dc1f493bcf3fff003b6df416dea4f41046e0f37d47
Status: Image is up to date for busybox:latest
Downloading image: busybox [OK]
Saving image: busybox
Saving image: busybox [OK]
127.0.0.1 - - [17/Jun/2018 12:27:42] "GET /dl?myimage=busybox HTTP/1.1" 200 -
```

If you specify the wget option "--content-disposition", you can get a proper image name on disk:

```
$ wget --content-disposition http://127.0.0.1:5000/dl?myimage=busybox
--2018-06-17 12:30:47--  http://127.0.0.1:5000/dl?myimage=busybox
Connecting to 127.0.0.1:5000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 47714304 (46M) [application/octet-stream]
Saving to: ‘busybox.tar’

busybox.tar                100%[=====================================>]  45.50M  --.-KB/s    in 0.1s    

2018-06-17 12:30:53 (423 MB/s) - ‘busybox.tar’ saved [47714304/47714304]
```

Curl
====

Add some curl examples here.

Todo
====

* multithreading with gunicorn, right now one client at a time
* docker image
* make a website to do the service with a proper letsencrypt https
* check the input format [az09] according to the docker spec
* investigate DIND to do the pull
* investigate other backends to download (udocker, curl scripts, etc...)
* use a curl script to download the image: https://github.com/moby/moby/blob/master/contrib/download-frozen-image-v2.sh
* web portal where you can specify the image+tag
