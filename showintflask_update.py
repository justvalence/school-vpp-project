#!flask/bin/python
from flask import Flask, jsonify
import subprocess
from flask import request
from flask import abort
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

@app.route('/vpp/api/tasks/up', methods=['PUT'])
def state_up():
        if not request.json or not 'getnameup' in request.json:
                abort(400)
        tasks = {'getnameup': request.json['getnameup']},
        getintUPname = str(request.json['getnameup'])
        setintstateUPcmd = 'sudo vppctl set interface state %s up' % (getintUPname)
        subprocess.call(setintstateUPcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
        return jsonify({'Output':'Command Executed'})

@app.route('/vpp/api/tasks/down', methods=['PUT'])
def state_down():
        if not request.json or not 'getnamedown' in request.json:
                abort(400)
        tasks = {'getnamedown': request.json['getnamedown']},
        getintDOWNname = str(request.json['getnamedown'])
        setintstateDOWNcmd = 'sudo vppctl set interface state %s down' % (getintDOWNname)
        subprocess.call(setintstateDOWNcmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
        return jsonify({'Output':'Command Executed'})

if __name__ == '__main__':
        app.run(debug=True)

