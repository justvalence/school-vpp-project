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

@vpp.route('/vpp/tasks/disable', methods=['PUT'])
@auth.login_required
def update_tasks_disable():

        task= {
                'ID': request.json['ID'],
                'Fwd': request.json['Fwd'],
                'U-Forwrd': request.json['U-Forwrd']
        }

        ID = str(request.json['ID'])
        Fwd = str(request.json['Fwd'])
        Disable = str(request.json['U-Forwrd'])
        Update = "sudo vppctl set bridge-domain %s %s %s" % (Fwd, ID, Disable)
        subp = subprocess.Popen(Update,stdout=subprocess.PIPE,shell=True)
        result = subp.communicate()[0]

        return ''

@vpp.route('/vpp/tasks/enable', methods=['PUT'])
@auth.login_required
def update_tasks_enable():

        task= {
                'ID': request.json['ID'],
                'Fwd': request.json['Fwd'],
                'U-Forwrd': request.json['U-Forwrd']
        }

        ID = str(request.json['ID'])
        Fwd = str(request.json['Fwd'])
        Enable = str(request.json['U-Forwrd'])
        Update = "sudo vppctl set bridge-domain %s %s %s" % (Fwd, ID, Enable)
        subp = subprocess.Popen(Update,stdout=subprocess.PIPE,shell=True)
        result = subp.communicate()[0]

        return ''

if __name__ == '__main__':
        vpp.run(debug=True)

