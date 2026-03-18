def log_request(request):
    print("User password:", request.form.get("password"))
