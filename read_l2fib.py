#!flask/bin/python
#!/user/bin/python
#!/bin/bash
from subprocesser_read_int import read_l2fib
import subprocess
from flask import Flask, jsonify, json, request
from flask import abort
from flask import make_response

app = Flask(__name__)




@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_l2fib():
	read_l2fib()
	task = "cat showl2fibtable.json"
        output = subprocess.Popen(task,shell=True,stdout=subprocess.PIPE)
        tasks = output.communicate()[0]
	if len(tasks) == 0:
		abort(404) 
	return tasks

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'No entries found'}), 404)

if __name__ == '__main__':
	app.run(debug=True)

