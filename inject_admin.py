#!/usr/bin/env python3

import ./inject.py

user = "admin"

user = inject_bypass(user)

params = {
    "u": user,
    "p": ""
}

url = "http://localhost/lab09/login.php"

(response, url_par) = send_request(params, url)

print(url_par)
print(response)
