from flask import Flask, request
import tensorflow as tf
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world"


@app.route("/predict", methods=['GET', 'POST'])
def predict():
	if 'file' not in request.files:
		print('No CSV file found')
		return "No file part"
	f = request.files['file']
	f.save(secure_filename(f.filename))
	hello=tf.constant('Hello world')
	sess = tf.Session()

	a = tf.constant(4)
	b = tf.constant(5)
	add = tf.add(a,b)
	return sess.run(hello)

if __name__ == '__main__':
	app.run(debug=True)

