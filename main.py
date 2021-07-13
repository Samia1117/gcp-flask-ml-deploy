from flask import Flask
from flask import jsonify

@app.route('/')
def hello():
	"""Return a friendly HTTP greeting"""
	print("I am inside hello!")
	return "Hello World (of Continuous Delivery)!"

@app.route('/echo/<name>')
def echo(name):
	print(f"This was placed in the url: new-{name}")
	val = {"new-name":name}
	return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
