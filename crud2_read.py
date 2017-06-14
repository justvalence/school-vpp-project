#!flask/bin/python
from flask import Flask,jsonify,abort,request
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
        if username == 'sti':
                return 'sti'
        return None

@auth.error_handler
def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)
import subprocess

app = Flask(__name__)

subpro = subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
res = subpro.communicate()[0]

tasks=res

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
        return tasks

if __name__ == '__main__':
        app.run(debug=True)

