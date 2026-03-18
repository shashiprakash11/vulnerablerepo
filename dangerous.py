import os
import pickle
import subprocess

def run_user_code(code):
    # ❌ Remote Code Execution
    eval(code)

def unsafe_deserialization(data):
    # ❌ Insecure deserialization
    return pickle.loads(data)

def command_exec(user_input):
    # ❌ Command Injection
    subprocess.call("ls " + user_input, shell=True)
