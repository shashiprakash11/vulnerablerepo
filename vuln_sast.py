import os
import hashlib
import requests

def sql_injection(user):
    query = "SELECT * FROM users WHERE name = '" + user + "'"
    return query

def command_injection(cmd):
    os.system("ping " + cmd)

def xss(user_input):
    return "<h1>" + user_input + "</h1>"

def weak_crypto(password):
    return hashlib.md5(password.encode()).hexdigest()

def path_traversal(filename):
    with open("/var/www/" + filename) as f:
        return f.read()

def ssrf(url):
    return requests.get(url).text

def debug_mode():
    debug = True
    return debug
