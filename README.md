# CERTIFICATE HANDLER


## For docker:

```sh
$ git clone https://github.com/toshamuravei/certhandler.git
$ sudo make build
$ cat >> settings.py
$ make run
$ make run CMD='ash'
$ python cert_handler.py
```
## For virtual environment:

```sh
$ git clone https://gitlab.oits.su/oits/certhandler.git
$ virtualenv .env -p python3.7
$ source .env/bin/activate
$ pip install -r requirements.txt
$ cat >> settings.py
$ python cert_handler.py
```
