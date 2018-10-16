from myapp.application import app
from flask import Flask,request,jsonify
from querymaker.query_builder import QueryBuilder
import json,csv
from api_tweet import Tweety
from configure import mappings
from csvconvert import json_to_csv
from store_tweet import common

@app.route('/')
def index():
	return '<h1>Welcome to TweetExtracter</h1>'


@app.route('/API1')
def streaming():
	result = dict()
	try:
		keywords = request.args.get('keywords')
		runtime = request.args.get('runtime')
		if keywords:
			keywords = keywords.split(",")
		else:
			result = {
				"status" : "failure"
			}
			return jsonify(result)
		Tweety().filter(keywords=keywords, runtime=runtime)
		result['status'] = "success"
		result['message'] = "Started streaming tweets with keywords {}".format(keywords)
	except Exception:
		result['status']="failure"
	return jsonify(result)



@app.route('/API2', methods=['GET', 'POST'])
def search_filter():
	res=common()
	return jsonify(res)



@app.route('/API3', methods=["GET", "POST"])
def jsontocsv():
	res=common()
	return json_to_csv(res)
