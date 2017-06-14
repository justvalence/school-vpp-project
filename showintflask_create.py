#!flask/bin/python
from flask import Flask, jsonify
import subprocess
from flask import request
from flask import abort
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

@app.route('/vpp/api/tasks', methods=['POST'])
def create_interface():
        if not request.json or not 'intname' in request.json:
                abort(400)

        task = {'intname': request.json['intname']}
        newint = str(request.json['intname'])
        createintcmd = 'sudo vppctl create host-interface name %s' % (newint)
        subprocess.call(createintcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
        return jsonify({'Output':'Command Executed'})


if __name__ == '__main__':
        app.run(debug=True)

