from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
	return jsonify({
		'message': 'Hi Dami',
		'time': datetime.datetime.today().strftime("%I:%M%p on %d-%m-%Y"),
		'host': socket.gethostname()
	})

@app.route('/api/v1/health')

def health():
	return jsonify({
		'status': 'Up'
	})

if __name__ == '__main__':
	app.run(host="0.0.0.0")
