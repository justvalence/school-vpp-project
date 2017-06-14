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


vpp = Flask(__name__)
cld = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
output = cld.communicate()[0]
tasks = output

@vpp.route('/vpp/tasks', methods=['POST'])
@auth.login_required
def create_loop():
        createl = 'sudo vppctl loopback create-interface'
        subprocess.call(createl,shell=True)
        return ''

if __name__ == '__main__':
        vpp.run(debug=True)


