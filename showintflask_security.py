#!flask/bin/python
from flask import Flask, jsonify
import subprocess
from flask import request
from flask import abort
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

@auth.get_password
def get_password(username):
        if username == 'user1':
                return 'python'
        return None

@auth.error_handler
def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)

if __name__ == '__main__':
        app.run(debug=True)

