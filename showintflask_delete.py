#!flask/bin/python
from flask import Flask, jsonify
import subprocess
from flask import request
from flask import abort
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

@app.route('/vpp/api/tasks', methods=['DELETE'])
def delete_interface():
        if not request.json or not 'name' in request.json:
                abort(400)
        tasks = {'name': request.json['name']}
        delint = str(request.json['name'])
        delintcmd = 'sudo vppctl delete host-interface name %s' % (delint)
        subprocess.call(delintcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
        return jsonify({'Output':'Command Executed'})

if __name__ == '__main__':
        app.run(debug=True)

