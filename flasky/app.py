import os
import random

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
	return 'Hello, World!'


## Returns a random number
@app.route('/random')
def random_number():
	return str((random.random() * 1000).__round__())


if __name__ == '__main__':
	print('Starting ' + os.path.basename(__file__) + ' at ' + os.getcwd() + '.')
	app.run(None, int(os.environ.get('PORT', 5002)), debug = True)
