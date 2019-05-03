from flask import Flask
from flask import request
app = Flask(__name__)

"""@app.route('/')

def hello_world():
	return "Hola mundo"
"""

@app.route('/hola-mundo')

def hello_world():
	nombre = request.args.get('nombre')
	return "Hola " + nombre

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
