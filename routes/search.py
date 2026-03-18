import os
from flask import request

def search():
    query = request.args.get("q")
    os.system("grep " + query + " data.txt")
    return "Search done"
