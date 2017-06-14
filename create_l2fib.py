#!flask/bin/python
#!/user/bin/python
#!/bin/bash
from subprocesser_create_int import add_l2fib
import subprocess
from flask import Flask, jsonify, json
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)



#GET METHOD - Retreive entries in the l2fib table
#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_l2fib():
#	read_l2fib()
#	task = "cat showl2fibtable.json"
#        output = subprocess.Popen(task,shell=True,stdout=subprocess.PIPE)
#        tasks = output.communicate()[0]
#	if len(tasks) == 0:
#		abort(404)
#	return tasks

#POST METHOD - Add new entry to the l2fib table
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_l2fib():
        if not request.json or not 'mac_address' or not 'bridge_domain_id' or not 'interface' or not 'state' in request.json:
                abort (400)

       	task = {
		'mac_address': request.json['mac_address'],
		'bridge_domain_id': request.json['bridge_domain_id'],
		'interface': request.json['interface'],
		'state': request.json['state']
	}
	
	mac_addr = str(request.json['mac_address'])
	bd_id = str(request.json['bridge_domain_id'])
	intf = str(request.json['interface'])
	stat = str(request.json['state'])

	add_l2fib(mac_addr, bd_id, intf, stat)

        return jsonify({'task':task}), 201

#DELETE METHOD - Clear all entries in the l2fib table
#@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
#def delete_l2fib():
#        del_l2fib()
#        task = "cat showl2fibtable.json"
#        output = subprocess.Popen(task,shell=True,stdout=subprocess.PIPE)
#        tasks = output.communicate()[0]
#        if len(tasks) > 0:
#                abort(403)
#        return jsonify({'Entries Deleted': True})


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'No entries found'}), 404)

@app.errorhandler(403)
def not_successful(error):
        return make_response(jsonify({'error': 'Entries not deleted'}), 403)

if __name__ == '__main__':
	app.run(debug=True)

