#! /usr/bin/env python3
# https://gist.github.com/sposterkil/8fcbd9d87d848b9666d7dacaa5573f4d#file-refreshurl-py

import webbrowser
from time import sleep

# url = input('Input the URL to reload, including "http://: ')
host = "localhost"
port = 8000
server_base_path = "/"
url = "http://%s:%d%s" % (host, port, server_base_path)

while True:
    print("refreshing...")
    webbrowser.open(url, new=0)
    sleep(3)
