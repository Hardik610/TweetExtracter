from myapp.application import app
from flask import Flask, request, jsonify
from querymaker.query_builder import QueryBuilder
import json, csv
from api_tweet import Tweety
from configure import mappings
from csvconvert import json_to_csv

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
				"status" : "failure",
			}
			return jsonify(result)
		Tweety().filter(keywords=keywords, runtime=runtime)
		result['status'] = "success"
		result['message'] = "Started streaming tweets with keywords {}".format(keywords)
	except Exception:
		result['status']="failure"
		result['message']=Exception.message
	return jsonify(result)



@app.route('/API2', methods=['GET', 'POST'])
def search_filter():
	elasticsearch_size = int(request.args.get('size',100))
	elasticsearch_from = int(request.args.get('from',0))
	data = json.loads(request.data)
	criteria =  data.get('criteria')
	sort = data.get('sort')
	s = QueryBuilder(criteria).search(index='tweets_index', doc_type='tweet')
	if sort:
		s=s.sort(*sort)
	s=s[elasticsearch_from:elasticsearch_size]
	try:
		elasticsearch_result=QueryBuilder.execute(s)
	except Exception:
		result = {
			"status" : "failure",
			"message" : Exception.message
		}
		return jsonify(result)
	result = dict()
	if elasticsearch_result is not None:
		hits = elasticsearch_result.hits
		result["count"] = {"total": hits.total, "fetched": len(hits.hits) }
		result["results"] = hits.hits
	return jsonify(result)


@app.route('/API3', methods=["GET", "POST"])
def jsontocsv():
	elasticsearch_size = int(request.args.get('size',100))
	elasticsearch_from = int(request.args.get('from',0))
	data = json.loads(request.data)
	criteria =  data.get('criteria')
	sort = data.get('sort')
	s = QueryBuilder(criteria).search(index='tweets_index', doc_type='tweet')
	if sort:
		s=s.sort(*sort)
	s=s[elasticsearch_from:elasticsearch_size]

	try:
		elasticsearch_result=QueryBuilder.execute(s)
	except Exception:
		result = {
			"status" : "failure",
			"message" : Exception.message
		}
		return jsonify(result)
	result = dict()

	if elasticsearch_result is not None:
		hits = elasticsearch_result.hits
		result["count"] = {"total": hits.total, "fetched": len(hits.hits) }
		result["results"] = hits.hits
	return json_to_csv(result)
