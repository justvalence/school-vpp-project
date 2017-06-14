#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'Zhenghan':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@auth.login_required

if __name__ == '__main__':
        vpp.run(debug=True)


