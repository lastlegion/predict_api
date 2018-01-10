from flask import Flask, request
import tensorflow as tf
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world"



''' POST API for prediction '''
@app.route("/predict", methods=['POST'])
def predict():
	if 'file' not in request.files:
		print('No CSV file found')
		return "No file part" 
	f = request.files['file'] #fetch file in the HTTP request
	f.save(secure_filename(f.filename)) # save file to disk
	
	''' Your tensorflow or black box code goes here'''
	hello=tf.constant('Hello world')
	sess = tf.Session()

	a = tf.constant(4)
	b = tf.constant(5)
	add = tf.add(a,b)
	''' End tensorflow code '''
	

	return sess.run(hello) # the response of POST goes here, it should return predicted values here.

if __name__ == '__main__':
	app.run(debug=True)

