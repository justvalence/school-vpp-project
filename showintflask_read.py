#!flask/bin/python
from flask import Flask, jsonify
import subprocess
from flask import request
from flask import abort
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

cmd = subprocess.Popen('cat showresult.json', stdout = subprocess.PIPE, shell = True)
output = cmd.communicate()[0]
intoutput = output

@app.route('/vpp/api/tasks', methods=['GET'])
@auth.login_required
def get_interface():
        return intoutput

if __name__ == '__main__':
        app.run(debug=True)

