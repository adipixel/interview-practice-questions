from flask import Flask, jsonify
app = Flask(__name__)

import json
from random import *

@app.route('/')
def hello_world():
	return 'Hello World! Please visit /roll/two/'


# generate random numbers for two dice rolls
@app.route('/roll/two/')
def rollTwo():
	# generating an object containing two random numbers
	# from range 1 to 6 inclusive
	roll = {"dice1": str(randint(1,6)), "dice2": str(randint(1,6))}
	# returning the JSON of the object created
	return jsonify(roll = roll)


if __name__ == '__main__':
	app.debug = True
	app.run()


