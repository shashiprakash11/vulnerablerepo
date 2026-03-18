from flask import request

def upload_file():
    file = request.files['file']
    file.save("uploads/" + file.filename)
    return "Uploaded"
