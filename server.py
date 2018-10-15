from myapp.application import app
import os

if __name__ == '__main__':
	app.secret_key = 'mysecret'
	app.run(host='0.0.0.0', port=8080, debug=True)